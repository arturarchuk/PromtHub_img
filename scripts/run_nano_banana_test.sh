#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required but was not found."
  exit 2
fi

if [ ! -f ".env" ]; then
  echo ".env is missing. Copy .env.example to .env and paste your API key."
  exit 2
fi

if grep -q "PASTE_YOUR_NEW_SECRET_HERE" ".env"; then
  echo "Open .env and replace PASTE_YOUR_NEW_SECRET_HERE with your new Google AI Studio API key."
  exit 2
fi

python3 -m pip install -r requirements.txt
python3 scripts/nano_banana_api_test.py
