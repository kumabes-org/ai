# Everything about artificial intelligence

## Fluxograma
```mermaid
graph TD
    Start(["🎯 Nova Necessidade / Tarefa com IA"]) --> Q_Ext{"Exige conectar com<br>sistemas externos?"}

    %% Ramo Externo
    Q_Ext -- SIM --> Q_MCP{"Precisa ser agnóstico<br>e padronizado entre<br>várias IDEs/clientes?"}
    Q_MCP -- SIM --> MCP["🔌 MCP (Model Context Protocol)<br><i>Ex: GitHub, Datadog, Postgres</i>"]
    Q_MCP -- NÃO --> Tool["🛠️ Tool / Function Calling<br><i>Ex: @tool write_file, run_pytest</i>"]

    %% Ramo Interno / Cognitivo
    Q_Ext -- NÃO --> Q_Prompt{"É apenas um ajuste<br>pontual ou formatação?"}
    Q_Prompt -- SIM --> Prompt["✍️ Prompt Engineering<br><i>Ex: Zero-shot, Few-shot, CoT</i>"]
    Q_Prompt -- NÃO --> Q_Skill{"É um procedimento<br>prescritivo com checklist<br>e template (SOP)?"}
    
    Q_Skill -- SIM --> Skill["📜 Skill (SKILL.md)<br><i>Ex: /adr-generator, /audit-k8s</i>"]
    Q_Skill -- NÃO --> Q_Agent{"Exige assumir papel,<br>tom de voz e limites<br>de atuação profissional?"}
    
    Q_Agent -- SIM --> Agent["👤 Agent / Persona (*.agent.md)<br><i>Ex: Solution Architect, Senior Dev</i>"]
    Q_Agent -- NÃO --> Multi["🤖 Multi-Agent / Grafo Autônomo<br><i>Ex: LangGraph Squad (Supervisor + Dev + SRE)</i>"]

    %% Estilos Visuais
    classDef decision fill:#1E293B,stroke:#64748B,stroke-width:2px,color:#F8FAFC;
    classDef outcome fill:#0F172A,stroke:#38BDF8,stroke-width:2px,color:#38BDF8;
    classDef startNode fill:#0284C7,stroke:#0284C7,stroke-width:2px,color:#FFFFFF;

    class Start startNode;
    class Q_Ext,Q_MCP,Q_Prompt,Q_Skill,Q_Agent decision;
    class MCP,Tool,Prompt,Skill,Agent,Multi outcome;
```

## Some Concepts

### O que é um modelo de IA?
Um modelo de IA é um "cérebro treinado em formato de arquivo" que aprendeu a reconhecer padrões e agora consegue responder perguntas, reconhecer imagens ou tomar decisões sem precisar de uma regra fixa programada para cada caso.

### O que é IA Generativa?
A IA Generativa é a capacidade da inteligência artificial de criar coisas novas (gerar texto, imagens, músicas, vídeos ou códigos) a partir de um pedido, em vez de apenas classificar ou escolher opções prontas.

### O que é IA Agêntica?
A IA Agêntica é quando a inteligência artificial deixa de ser apenas uma "conversa passiva" (que só responde e espera) e passa a ter iniciativa, capacidade de tomar decisões e usar ferramentas no mundo real para cumprir um objetivo completo.

### O que é LLM (Large Language Model / Grande Modelo de Linguagem)?
Um LLM é o "motor" ou a base de conhecimento. Trata-se de um supercomputador treinado com quase todo o texto público da internet (livros, artigos, conversas, códigos). Ele aprendeu os padrões da linguagem humana tão bem que consegue prever e combinar palavras de forma natural e coerente.

### O que é Tool?
A IA por si só só consegue pensar e escrever. Quando damos uma Tool a ela, ela ganha o poder de agir no mundo real: usar uma calculadora para não errar contas, consultar a previsão do tempo na internet, ler uma planilha ou enviar um e-mail de verdade.

### O que é um prompt?
Um Prompt é a pergunta, comando ou pedido que você faz para a Inteligência Artificial.
- Zero-Shot:                Perguntas diretas e simples
- Few-Shot:                 Padronizar formatos e regras estritas de saída
- Chain-of-Thought (CoT):   Cálculos, algoritmos e problemas lógicos
- Role Prompting:           Mudar tom de voz e profundidade técnica
- Tree of Thoughts (ToT):   Tomada de decisão complexa e estratégias

### O que é um MCP?
O MCP é a tomada padrão que permite que a IA se conecte com segurança aos seus sistemas corporativos e bancos de dados (como arquivos da empresa, e-mails, sistemas de nuvem ou GitHub) sem precisar programar uma conexão complicada e diferente para cada um.

### O que é um Skill?
É um procedimento salvo que diz à IA: "Toda vez que eu pedir para revisar um documento, siga este checklist de 5 itens e me entregue a resposta neste modelo de tabela".

### O que é RAG?
O RAG (Retrieval Augmented Generation). Em vez de a IA tentar adivinhar ou lembrar o que aprendeu meses atrás, o RAG permite que ela consulte os documentos particulares da sua empresa (manuais, PDFs, contratos) em tempo real antes de responder, garantindo que a resposta seja exata, atualizada e sem invenções.

### O que é Loop Engineer?
Loop Engineer é quem constrói o sistema que permite à Inteligência Artificial executar uma tarefa, testar o próprio resultado, corrigir os próprios erros e tentar de novo em repetição (em loop), até entregar o trabalho perfeito sem precisar de um humano dizendo o que fazer a cada minuto.

### O que é Harness Engineering?
Harness Engineering é a disciplina de construir o ambiente de segurança, regras, testes e ferramentas ao redor da Inteligência Artificial, garantindo que ela trabalhe sozinha de forma confiável, corrija seus próprios erros e entregue o resultado perfeito sem quebrar nada.

### O que é LangGraph?
É um sistema que define as regras exatas de um processo com paradas, revisões e voltas. Se a IA escreve um texto, o LangGraph manda esse texto para a etapa de revisão; se o revisor achar um erro, o sistema devolve o trabalho para o redator corrigir antes de finalizar. Ele garante que tarefas complexas sigam uma ordem rígida e não se percam.

### O que é AutoGen?
Criado pela Microsoft, o AutoGen permite que diferentes IAs conversem umas com as outras em um bate-papo em grupo. Uma IA dá uma ideia, a outra critica, uma terceira testa e elas continuam dialogando até chegarem juntas à melhor solução, sem precisar que você fique intermediando cada frase.

### O que é CrewAI?
O CrewAI organiza as IAs como se fossem funcionários de uma empresa. Você define: "Você é o Pesquisador e sua missão é achar dados", "Você é o Redator e sua missão é escrever o artigo" e "Você é o Gerente que aprova a entrega". Ele foca em fazer essa equipe colaborar de forma simples e direta para entregar um projeto pronto.

### O que é Langfuse?
Quando você coloca IAs para trabalhar, precisa saber se elas estão funcionando direito. O Langfuse monitora tudo nos bastidores: grava o que foi perguntado e respondido, avisa se a resposta demorou muito, mostra quanto dinheiro em processamento aquela conversa custou e ajuda a identificar se a IA cometeu algum erro.

| Critério | Workflows | LangChain | LangGraph | CrewAI |
| :--- | :--- | :--- | :--- | :--- |
| **Nível de Abstração** | Baixo / Conceitual | Médio (Blocos fundamentais) | Médio / Baixo (Controle de baixo nível) | Alto (Orientado a pessoas/papéis) |
| **Controle de Fluxo** | Rígido e linear | Linear (*Chains* sequenciais) | Cíclico, ramificado e com loops | Colaborativo entre agentes |
| **Poder de Decisão da IA** | Mínimo (segue código fixo) | Médio (decisões pontuais) | Alto (decide o próximo nó do grafo) | Alto (resolve tarefas em equipe) |
| **Suporte a Loops e Auto-correção** | Manual no código | Fraco / Complexo | Nativo e robusto | Nativo |
| **Melhor Caso de Uso** | Pipelines ETL e validações simples | Conectar APIs, RAG simples e prompts | Squads complexas, SRE e sistemas críticos | Automação de marketing, pesquisa e redação |

## Criando virtual environment
```
py -3.12 -m venv .venv
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Universal Directory Structure (.ai/ or .agent/)
```
meu-projeto/
├── .agent/                      # Pasta agnóstica centralizada
│   ├── rules/                   # Regras globais de engenharia
│   │   ├── code-standards.md
│   │   └── security.md
│   ├── personas/                # Definição dos agentes
│   │   ├── architect.md
│   │   ├── developer.md
│   │   └── product-manager.md
│   └── skills/                  # Procedimentos e runbooks
│       ├── run-tests/
│       │   └── SKILL.md
│       └── pr-review/
│           └── SKILL.md
│
├── .mcp/
│   └── config.json              # Configuração agnóstica de servidores MCP
│
├── AGENTS.md                    # Ponto de entrada universal para qualquer agente
│
# Bridges / Links Simbólicos para ferramentas específicas:
├── .cursorrules                 # -> Aponta para .agent/rules/code-standards.md
├── .github/
│   ├── copilot-instructions.md  # -> Aponta para .agent/rules/code-standards.md
│   └── skills/                  # -> Link ou cópia de .agent/skills/
└── CLAUDE.md                    # -> Aponta para AGENTS.md
```


|Skill	                                |Escopo Principal	    |Impacto Organizacional|
|-------------|-------------|-------------|
|adr-generator	                        |Arquitetura de Software|Governança técnica e histórico de decisões transparente.|
|k8s-platform-policy-guard	            |Platform Engineering	|Redução drástica de falhas de deploy e vulnerabilidades em cluster.|
|slo-datadog-monitor-designer	        |SRE & Operações	    |Padronização de observabilidade sem esforço manual das squads.|
|iac-security-and-finops-auditor	    |Cloud / DevOps	        |Segurança em camadas e controle de custos de infraestrutura.|
|api-contract-breaking-change-detector	|Integrações / SDD	    |Eliminação de indisponibilidades por incompatibilidade de contratos.|
|incident-postmortem-copilot	        |Cultura de Engenharia	|Resiliência sistêmica contínua e aprendizado pós-falha.|