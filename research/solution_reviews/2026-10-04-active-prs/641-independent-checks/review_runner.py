from pathlib import Path
import copy, json, subprocess, sys
HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parents[3]/"research"/"solutions"/"siavash-sadeghi-641"
results=[]
for optimized in (False,True):
    mode="optimized" if optimized else "normal"
    for filename in ("verify_cubic.py","check_printed_table.py","crosscheck_cubic.py","test_verifier.py"):
        command=[sys.executable]+(["-O"] if optimized else [])+[str(PACKAGE/filename)]
        run=subprocess.run(command,capture_output=True,text=True)
        log=HERE/(filename[:-3]+"-"+mode+".log")
        log.write_text("COMMAND "+repr(command)+"\nEXIT "+str(run.returncode)+"\nSTDOUT\n"+run.stdout+"\nSTDERR\n"+run.stderr,encoding="utf-8")
        results.append({"test":filename,"mode":mode,"exit":run.returncode,"log":log.name})
        if run.returncode: raise ArithmeticError("Reproduction failed "+str(results[-1]))
    if optimized:
        command=[sys.executable,"-O",str(HERE/"independent_checks.py")]
        run=subprocess.run(command,capture_output=True,text=True)
        log=HERE/"independent-optimized.log"
        log.write_text("COMMAND "+repr(command)+"\nEXIT "+str(run.returncode)+"\nSTDOUT\n"+run.stdout+"\nSTDERR\n"+run.stderr,encoding="utf-8")
        results.append({"test":"independent_checks.py","mode":mode,"exit":run.returncode,"log":log.name})
        if run.returncode: raise ArithmeticError("Independent optimized audit failed")
    # Supplied unittest damages the table only in optimized mode.
    # This fresh check verifies rejection in both modes.
    paper=(PACKAGE/"aim641_report.tex").read_text(encoding="utf-8")
    damaged=paper.replace("$(691,111)$","$(692,111)$")
    if damaged==paper: raise ArithmeticError("Damage not applied")
    damaged_file=HERE/"damaged-printed-table.tex"
    damaged_file.write_text(damaged,encoding="utf-8")
    command=[sys.executable]+(["-O"] if optimized else [])+[str(PACKAGE/"check_printed_table.py"),"--paper",str(damaged_file)]
    run=subprocess.run(command,capture_output=True,text=True)
    log=HERE/("damaged-printed-table-"+mode+".log")
    log.write_text("COMMAND "+repr(command)+"\nEXIT "+str(run.returncode)+"\nSTDOUT\n"+run.stdout+"\nSTDERR\n"+run.stderr,encoding="utf-8")
    if run.returncode==0 or "Printed polynomial mismatch" not in run.stderr:
        raise ArithmeticError("Printed corruption not rejected")
    results.append({"test":"fresh printed-table corruption","mode":mode,"exit":run.returncode,"expected_failure":True,"log":log.name})
    # A perturbation vanishing at M=8 challenges the finite crosscheck's scope.
    original=json.loads((PACKAGE/"cubic_certificate.json").read_text(encoding="utf-8"))
    challenge=copy.deepcopy(original)
    challenge[0]["coefficient"]="("+challenge[0]["coefficient"]+")+(M-8)"
    challenge_file=HERE/"dimension-challenge-certificate.json"
    challenge_file.write_text(json.dumps(challenge),encoding="utf-8")
    command=[sys.executable]+(["-O"] if optimized else [])+[str(PACKAGE/"verify_cubic.py"),"--check-certificate",str(challenge_file)]
    run=subprocess.run(command,capture_output=True,text=True)
    log=HERE/("dimension-challenge-"+mode+".log")
    log.write_text("COMMAND "+repr(command)+"\nEXIT "+str(run.returncode)+"\nSTDOUT\n"+run.stdout+"\nSTDERR\n"+run.stderr,encoding="utf-8")
    if run.returncode==0 or "Saved certificate differs" not in run.stderr:
        raise ArithmeticError("Dimension challenge not rejected")
    results.append({"test":"symbolic dimension challenge +(M-8)","mode":mode,"exit":run.returncode,"expected_failure":True,"log":log.name})
(HERE/"fresh-reproduction-results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
print(json.dumps(results,indent=2))
print("ALL FRESH REPRODUCTIONS AND EXPECTED-FAILURE CHECKS PASSED")
