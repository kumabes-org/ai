#!/usr/bin/env bash
set -euo pipefail

if [[ -x ".venv/Scripts/python.exe" ]]; then
	PYTHON=".venv/Scripts/python.exe"
elif [[ -x ".venv/bin/python" ]]; then
	PYTHON=".venv/bin/python"
else
	PYTHON="python"
fi

echo "🔍 [HARNESS] 1. Executando Linter e Análise Estática..."
"$PYTHON" -m ruff check .
"$PYTHON" -m ruff format --check .

echo "🔒 [HARNESS] 2. Verificando Tipagem Estrita..."
"$PYTHON" -m mypy src/

echo "🧪 [HARNESS] 3. Executando Testes e Cobertura..."
"$PYTHON" -m pytest --cov=src --cov-fail-under=90 tests/

echo "✅ [HARNESS] Todas as verificações passaram com sucesso!"