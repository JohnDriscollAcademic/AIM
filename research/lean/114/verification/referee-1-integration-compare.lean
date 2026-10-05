import Lean

/-!
Local operational audit of separately imported Challenge and Solution environments.
This is not the sandboxed export/kernel Comparator. It supplements that gate by
checking actual elaborated statement and referenced-constant equality locally.

Comparison traversal follows the hash-locked Comparator.Compare and Comparator.Util
algorithm, Copyright (c) 2025 Lean FRO, LLC, authors Henrik Böving, Apache-2.0,
Forsythe revision 8d1b0c0545a77b40245e84705aa7d273e6c81e62.
-/

open Lean

deriving instance BEq for Lean.QuotKind
deriving instance BEq for Lean.QuotVal
deriving instance BEq for Lean.InductiveVal
deriving instance BEq for Lean.ConstantInfo

private def requireExcept {α : Type} (x : Except String α) : IO α :=
  match x with
  | .ok v => pure v
  | .error e => throw <| IO.userError e

private def getConst (env : Environment) (n : Name) : IO ConstantInfo :=
  match env.find? n with
  | some c => pure c
  | none => throw <| IO.userError s!"Constant absent: {n}"

private def dependencies (c : ConstantInfo) : Array Name := Id.run do
  let mut out := c.type.getUsedConstants.push c.name
  if let some v := c.value? (allowOpaque := true) then
    out := out ++ v.getUsedConstants
  match c with
  | .inductInfo v => out := out ++ v.ctors.toArray ++ v.all.toArray
  | .ctorInfo v => out := out.push v.induct
  | .recInfo v =>
    for rule in v.rules do
      out := out.push rule.ctor ++ rule.rhs.getUsedConstants
  | _ => pure ()
  return out

def main : IO Unit := do
  initSearchPath (← findSysroot)
  let cfg ← requireExcept <| Json.parse (← IO.FS.readFile "comparator.json")
  let namesJson ← requireExcept <| (← requireExcept <| cfg.getObjVal? "theorem_names").getArr?
  let mut names : Array Name := #[]
  for j in namesJson do
    names := names.push (← requireExcept j.getStr?).toName
  let challenge ← importModules #[{ module := `Challenge }] {}
  let solution ← importModules #[{ module := `Solution }] {}
  let bad := solution.header.moduleNames.filter fun n => n.toString.endsWith "Challenge"
  unless bad.isEmpty do
    throw <| IO.userError s!"Challenge module in Solution import closure: {bad}"
  IO.println s!"Solution actual imported module closure: {solution.header.moduleNames.size} modules; no Challenge."
  let targets := Std.HashSet.ofArray names
  let mut pending : Array Name := #[]
  for n in names do
    let cc ← getConst challenge n
    let sc ← getConst solution n
    match cc, sc with
    | .thmInfo c, .thmInfo s =>
      unless c.toConstantVal == s.toConstantVal do
        throw <| IO.userError s!"Actual theorem statement mismatch: {n}"
      pending := pending ++ c.type.getUsedConstants
      IO.println s!"Exact elaborated theorem statement PASS: {n}"
    | _, _ => throw <| IO.userError s!"Expected theorem in both environments: {n}"
  let mut checked : Std.HashSet Name := {}
  let mut localConstants : Array Name := #[]
  while !pending.isEmpty do
    let n := pending.back!
    pending := pending.pop
    if checked.contains n then continue
    let cc ← getConst challenge n
    let sc ← getConst solution n
    if targets.contains n then
      pending := pending ++ sc.type.getUsedConstants
    else
      unless cc == sc do
        throw <| IO.userError s!"Referenced constant closure mismatch: {n}"
      pending := pending ++ dependencies sc
    if n.toString.startsWith "AIM.P114." then
      localConstants := localConstants.push n
    checked := checked.insert n
  IO.println s!"Exact referenced-constant closure PASS: {checked.size} constants."
  for n in localConstants do
    IO.println s!"Project closure constant: {n}"
  IO.println s!"Local integration comparison PASS: {names.size} actual declarations."
