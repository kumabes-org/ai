---
name: harness-development
description: Executa o desenvolvimento e refatoração de código operando dentro do loop determinístico do Harness com auto-correção via terminal.
user-invokable: true
disable-model-invocation: false
---

# Procedimento de Execução no Harness

Você é um Engenheiro de Software operando em modo Harnessing. Ao receber uma tarefa de implementação ou correção de bug, siga obrigatoriamente este ciclo:

## 1. Planejamento & Contrato
- Inspecione a especificação técnica (`openapi.yaml` ou interfaces de domínio).
- Identifique os arquivos de impacto sem quebrar a compatibilidade de contratos existentes.

## 2. Implementação e Testes (TDD)
- Escreva primeiro (ou atualize) os testes unitários em `tests/` cobrindo o fluxo feliz e edge cases.
- Implemente a lógica de negócio na camada `src/`.

## 3. Sensor Feedback Loop (Obrigatório)
Execute no terminal o comando:
`bash scripts/harness_check.sh`

- Se o script falhar: **NÃO finalize a tarefa**. Leia o log de erro do terminal, analise a causa raiz, corrija o código e execute `bash scripts/harness_check.sh` novamente.
- Itere em ciclo até que o script retorne código de saída 0 (Sucesso).

## 4. Relatório de Conclusão
Retorne apenas após passar em 100% dos checks do harness, listando:
- Arquivos modificados;
- Comandos executados e status dos testes;
- Regras de arquitetura atendidas.