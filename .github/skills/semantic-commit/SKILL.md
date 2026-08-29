# Skill: Conventional Commit Generator

## Objetivo
Analisar o diff do Git e gerar uma mensagem de commit semântica precisa.

## Regras de Validação
1. Formato estrito: `<tipo>(<escopo>): <descrição no imperativo>`
2. Tipos aceitos: feat, fix, docs, style, refactor, perf, test, build, ci, chore.
3. Máximo de 72 caracteres na primeira linha.
4. Não utilize ponto final no título.
5. Se houver Breaking Change, inclua `!` antes dos dois pontos ou no rodapé.

## Exemplo de Saída
feat(workflow): Criação e validação do workflow de ci-cd java maven eks