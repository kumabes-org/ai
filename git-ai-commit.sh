#!/usr/bin/env bash

set -e

# Caminho para o arquivo da Skill
SKILL_PATH="./.github/skills/semantic-commit/SKILL.md"

# 1. Verifica se a API Key está configurada
if [ -z "$GEMINI_API_KEY" ]; then
  echo "❌ Erro: A variável de ambiente GEMINI_API_KEY não está definida."
  echo "Exporte com: export GEMINI_API_KEY='sua-chave-aqui'"
  exit 1
fi

# 2. Verifica se o arquivo da Skill existe
if [ ! -f "$SKILL_PATH" ]; then
  echo "❌ Erro: Arquivo de Skill não encontrado em: $SKILL_PATH"
  exit 1
fi

# 3. Captura as alterações staged
DIFF=$(git diff --cached)

if [ -z "$DIFF" ]; then
  echo "⚠️  Nenhuma alteração em 'staged'. Execute 'git add <arquivos>' antes de rodar o gerador."
  exit 1
fi

echo "🔍 Lendo Skill e analisando alterações staged..."

# 4. Monta o prompt combinando a Skill + o Diff
SKILL_CONTENT=$(cat "$SKILL_PATH")

# Sanitiza as entradas para JSON
PROMPT_PAYLOAD=$(jq -n \
  --arg skill "$SKILL_CONTENT" \
  --arg diff "$DIFF" \
  '{
    contents: [
      {
        parts: [
          {
            text: ($skill + "\n\nAnalise o seguinte git diff staged e retorne APENAS a mensagem de commit semântica final (sem blocos de código markdown, sem aspas, sem texto explicativo adicional):\n\n" + $diff)
          }
        ]
      }
    ],
    generationConfig: {
      temperature: 0.1
    }
  }')

# 5. Faz a chamada para a API do Gemini via curl
API_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}"

RESPONSE=$(curl -s -X POST "$API_URL" \
  -H "Content-Type: application/json" \
  -d "$PROMPT_PAYLOAD")

# 6. Extrai a resposta gerada
COMMIT_MSG=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text' | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

if [ -z "$COMMIT_MSG" ] || [ "$COMMIT_MSG" = "null" ]; then
  echo "❌ Erro ao gerar a mensagem. Resposta da API:"
  echo "$RESPONSE"
  exit 1
fi

echo ""
echo "✨ Mensagem de commit sugerida pela Skill:"
echo "--------------------------------------------------------"
echo "$COMMIT_MSG"
echo "--------------------------------------------------------"
echo ""

# 7. Interação com o usuário: Confirmar, Editar ou Cancelar
read -p "Deseja realizar o commit com esta mensagem? [S/e/n] (S=Sim, e=Editar, n=Cancelar): " CHOICE
CHOICE=${CHOICE:-S}

case "$CHOICE" in
  [sS]*)
    git commit -m "$COMMIT_MSG"
    echo "✅ Commit realizado com sucesso!"
    ;;
  [eE]*)
    read -e -i "$COMMIT_MSG" -p "Edite a mensagem: " EDITED_MSG
    git commit -m "$EDITED_MSG"
    echo "✅ Commit realizado com sucesso!"
    ;;
  *)
    echo "🚫 Operação cancelada. Nenhum commit realizado."
    exit 0
    ;;
esac