#!/usr/bin/env bash
# Re-run the certified computation of PROOF.md and record its log.
set -euo pipefail
cd "$(dirname "$0")"
python3 certify/main.py 2>&1 | tee logs/certify.log
