"""Read-only independent PR33 evidence audit; outputs stay beside this script."""
from pathlib import Path
import concurrent.futures
import hashlib
import io
import json
import re
import subprocess
import sys
import tarfile
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent
SNAP = ROOT / "pr33"
REPO = Path("C:/Users/MatthewColbrook/Documents/git_repos/AIM")
PROJECT = SNAP / "research/lean/114"
EVIDENCE = PROJECT / "verification/linux-2026-10-05-final-31"
OUT = ROOT / "pr33-formal-independent-evidence"
OUT.mkdir(exist_ok=True)
HEAD = "61916d1e9959dc7ed282edb124b51e8118735844"
RUN_HEAD = "56afd77d2456af3da7934947699ee86735494010"

def run(*args):
    return subprocess.run(args, cwd=REPO, check=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).stdout

def digest(data):
    return hashlib.sha256(data).hexdigest()

_git_files = {}
def blob(rev, path):
    if rev not in _git_files:
        tree = run("git","ls-tree","-r","-z",rev)
        entries = []
        for entry in tree.split(b"\0"):
            if entry:
                meta,name = entry.split(b"\t",1)
                mode,kind,oid = meta.split()
                if kind == b"blob":
                    entries.append((name.decode(),oid))
        batch = subprocess.run(["git","cat-file","--batch"],cwd=REPO,check=True,
            input=b"\n".join(oid for _,oid in entries)+b"\n",stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
        decoded = {}
        cursor = 0
        for name,oid in entries:
            end = batch.index(b"\n",cursor)
            header = batch[cursor:end].split()
            size = int(header[2])
            cursor = end+1
            decoded[name] = batch[cursor:cursor+size]
            cursor += size+1
        _git_files[rev] = decoded
    return _git_files[rev][path]

def api(path):
    return json.loads(run("gh", "api", path))

fresh = {}
for kind, suffix in [("run", ""), ("jobs", "/jobs"), ("artifacts", "/artifacts")]:
    data = api(f"repos/sidneyholden1/AIM/actions/runs/37365344243{suffix}")
    fresh[kind] = data
    (OUT / f"github-{kind}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")

summary = {"reviewed_head": HEAD, "verified_revision": RUN_HEAD,
           "fresh_run": {k:fresh["run"][k] for k in ["id", "head_sha", "status", "conclusion", "event", "html_url"]},
           "fresh_jobs": [{k:j[k] for k in ["id", "name", "head_sha", "status", "conclusion", "labels"]} for j in fresh["jobs"]["jobs"]]}
summary["artifact_checks"] = []
for artifact in fresh["artifacts"]["artifacts"]:
    name = artifact["name"]
    retained = EVIDENCE / f"{name}.zip"
    downloaded = run("gh", "api", f"repos/sidneyholden1/AIM/actions/artifacts/{artifact['id']}/zip")
    (OUT / f"{name}-fresh.zip").write_bytes(downloaded)
    z = zipfile.ZipFile(io.BytesIO(downloaded))
    member_checks = []
    for member in z.namelist():
        if member.endswith("/"):
            continue
        retained_member = EVIDENCE / name / member
        git_member = "research/lean/114/verification/linux-2026-10-05-final-31/"+name+"/"+member
        member_checks.append({"path":member, "sha256":digest(z.read(member)),
                              "retained_match":z.read(member) == blob(HEAD,git_member),
                              "snapshot_exact_match":retained_member.exists() and z.read(member) == retained_member.read_bytes(),
                              "snapshot_matches_after_crlf_normalization":retained_member.exists() and z.read(member) == retained_member.read_bytes().replace(b"\r\n",b"\n")})
    summary["artifact_checks"].append({"name":name, "id":artifact["id"],
        "api_digest":artifact.get("digest"), "download_sha256":digest(downloaded),
        "api_digest_match":artifact.get("digest") == "sha256:"+digest(downloaded),
        "retained_zip_match":downloaded == retained.read_bytes(), "members":member_checks})

result = json.loads(next((EVIDENCE / "lean-114").glob("verify-*/result.json")).read_text())
summary["verified_result"] = {k:v for k,v in result.items() if k != "input_sha256"}
summary["input_hash_checks"] = []
with tarfile.open(EVIDENCE / "source.tar.gz", "r:gz") as tar:
    files = {m.name.split("/",1)[1]:tar.extractfile(m).read() for m in tar if m.isfile() and "/" in m.name}
    summary["source_archive"] = {"sha256":digest((EVIDENCE / "source.tar.gz").read_bytes()), "file_count":len(files)}
    archive_mismatches = []
    for path,data in files.items():
        try:
            if blob(RUN_HEAD,"research/lean/114/"+path) != data:
                archive_mismatches.append(path)
        except (subprocess.CalledProcessError, KeyError):
            archive_mismatches.append(path)
    summary["source_archive"]["git_revision_mismatches"] = archive_mismatches
    for path,expected in result["input_sha256"].items():
        repo_path = "research/lean/114/"+path
        verified_bytes = blob(RUN_HEAD,repo_path)
        current_bytes = blob(HEAD,repo_path)
        row = {"path":path,"expected":expected,"verified_git_match":digest(verified_bytes)==expected,
               "archive_match":digest(files[path])==expected,
               "current_head_match":digest(current_bytes)==expected,
               "snapshot_matches_head":(PROJECT/path).read_bytes()==current_bytes,
               "snapshot_matches_head_after_crlf_normalization":(PROJECT/path).read_bytes().replace(b"\r\n",b"\n")==current_bytes}
        summary["input_hash_checks"].append(row)

summary["later_changes"] = run("git","diff","--name-status",RUN_HEAD,HEAD).decode().splitlines()
summary["checker_changes_vs_upstream"] = run("git","diff","--name-status","origin/main",HEAD,"--",
    "tools/lean",".github/workflows/lean-verification.yml",".github/workflows/lean-statements.yml","docs/lean/schema").decode().splitlines()
summary["source_lock_receipt_matches"] = digest(blob(HEAD,"tools/lean/source-lock.json")) == result["source_lock_sha256"]

config = json.loads((PROJECT/"comparator.json").read_text())
challenge = (PROJECT/"Challenge.lean").read_text(encoding="utf-8")
challenge_names = re.findall(r"^theorem\s+([\w']+)",challenge,re.M)
proof_names = []
imports = {}
blocked_tokens = {}
for p in (PROJECT/"AIM/P114").glob("*.lean"):
    source = p.read_text(encoding="utf-8")
    imports[p.name] = re.findall(r"^import\s+(.+)",source,re.M)
    proof_names += re.findall(r"^theorem\s+([\w']+)",source,re.M)
    without_comments = re.sub(r"/\-.*?\-/", "", source, flags=re.S)
    without_comments = re.sub(r"--[^\n]*", "", without_comments)
    tokens = re.findall(r"\b(?:sorry|admit|axiom|native_decide|unsafe|implemented_by)\b",without_comments)
    if tokens:
        blocked_tokens[p.name] = tokens
expected = ["AIM.P114."+n for n in challenge_names]
summary["coverage"] = {"challenge_count":len(challenge_names),"proof_count":len(proof_names),
    "comparator_count":len(config["theorem_names"]),"challenge_matches_comparator":expected==config["theorem_names"],
    "proof_set_matches_comparator":set("AIM.P114."+n for n in proof_names)==set(config["theorem_names"]),
    "config_matches_verified_result":config==result["config"],"definition_names":config["definition_names"],
    "permitted_axioms":config["permitted_axioms"],"blocked_tokens_in_mathematical_source":blocked_tokens,"imports":imports}
summary["reviewed_file_sha256"] = {str(p.relative_to(SNAP)).replace("\\","/"):digest(blob(HEAD,str(p.relative_to(SNAP)).replace("\\","/")))
    for p in PROJECT.rglob("*") if p.is_file() and (p.suffix==".lean" or p.name in ["NUMERICAL_TARGETS.md","comparator.json","formalization.yaml","lake-manifest.json","lakefile.toml","lean-toolchain"])}

lock = json.loads((SNAP/"tools/lean/source-lock.json").read_text())
def upstream_check(item):
    endpoint = f"repos/sgstepaniants/Forsythe/contents/{item['source']}?ref={lock['commit']}"
    data = run("gh","api","-H","Accept: application/vnd.github.raw+json",endpoint)
    return {"source":item["source"],"sha256":digest(data),"matches_lock":digest(data)==item["sha256"],"bytes_match":len(data)==item["bytes"]}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    summary["fresh_forsythe_source_lock_checks"] = list(executor.map(upstream_check,lock["files"]))

from pypdf import PdfReader
pdf = SNAP/"research/solutions/114-nodal-surplus-counterexample/submitted/short_proof-v0.3.pdf"
reader = PdfReader(pdf)
summary["source_pdf"] = {"sha256":digest(pdf.read_bytes()),"pages":len(reader.pages)}
(OUT/"submitted-manuscript-text.txt").write_text("\n\n".join(f"PAGE {i+1}\n"+p.extract_text() for i,p in enumerate(reader.pages)),encoding="utf-8")
manifest_text = (PROJECT/"formalization.yaml").read_text(encoding="utf-8")
main_block = manifest_text.split("  main_results:",1)[1].split("\nfidelity:",1)[0]
main_names = re.findall(r"^  - declaration: (\S+)",main_block,re.M)
summary["manifest_coverage"] = {"main_result_count":len(main_names),
    "ordered_names_match_comparator":main_names==config["theorem_names"],
    "method":"Text extraction of declaration fields; full YAML schema validation is separate",
    "sorry_count":re.findall(r"^  sorry_count: (\d+)",manifest_text,re.M),
    "sorry_in_definitions":re.findall(r"^  sorry_in_definitions: (\d+)",manifest_text,re.M)}
with zipfile.ZipFile(OUT/"lean-114-fresh.zip") as z:
    comparator_text = z.read(next(n for n in z.namelist() if n.endswith("/comparator.log"))).decode()
axioms = {n:[a.strip() for a in values.split(",")] for n,values in
    re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",comparator_text)}
summary["axiom_log"] = {"target_count":len(axioms),
    "names_match_comparator":set(axioms)==set(config["theorem_names"]),
    "only_permitted_axioms":all(set(a)<=set(config["permitted_axioms"]) for a in axioms.values()),
    "transitive_axioms":axioms}
summary["mechanical_reexecution_by_this_reviewer"] = False
(OUT/"audit.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps({"output":str(OUT),"coverage":summary["coverage"],
    "artifact_checks":[{k:v for k,v in a.items() if k != "members"} | {"all_members_match":all(m["retained_match"] for m in a["members"])} for a in summary["artifact_checks"]],
    "source_archive":summary["source_archive"],"input_count":len(summary["input_hash_checks"]),
    "input_failures":[r for r in summary["input_hash_checks"] if not r["verified_git_match"] or not r["archive_match"]],
    "head_changed_inputs":[r["path"] for r in summary["input_hash_checks"] if not r["current_head_match"]],
    "forsythe_file_count":len(summary["fresh_forsythe_source_lock_checks"]),
    "forsythe_failures":[r for r in summary["fresh_forsythe_source_lock_checks"] if not r["matches_lock"] or not r["bytes_match"]]},indent=2))
