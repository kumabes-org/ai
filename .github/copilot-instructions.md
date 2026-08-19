# Repository Harness Constraints

- Toda e qualquer implementação deve passar sem exceções em `bash scripts/harness_check.sh`.
- Nunca apague ou desative um teste existente para fazer o build passar.
- Se você encontrar uma falha de lint ou type hint durante o Agent Mode, use o terminal para auto-corrigir antes de entregar a resposta ao usuário.

# Diretrizes Gerais de Desenvolvimento em Python

Você atua como um assistente de engenharia sênior. Ao gerar, refatorar ou analisar código Python neste repositório, siga estritamente os padrões, restrições e convenções descritos abaixo.

---

## 1. Padrões de Linguagem & Estilo de Código

- **Versão:** Python 3.12+ (utilize recursos modernos como `match/case`, novos operadores de union type `X | Y`, e sintaxe atualizada de generics).
- **Tipagem Obrigatória (Strict Type Hinting):**
  - Todas as funções, métodos e atributos de classe devem conter anotações de tipo explícitas para parâmetros e retorno.
  - Utilize módulos padrão como `typing` e `collections.abc` (ex: `Sequence`, `Mapping`, `Callable`, `Iterable`).
  - Nunca utilize `Any` a menos que seja estritamente indispensável; prefira `TypeVar`, `Generic` ou unions específicas.
- **Modelagem de Dados & Schemas:**
  - Utilize **Pydantic v2** (`BaseModel`, `Field`, `ConfigDict`) para validação de contratos, dados de entrada/saída e variáveis de ambiente (`pydantic-settings`).
  - Para estruturas de dados internas imutáveis, utilize `dataclasses` com `frozen=True`.
- **Formatação e Linting:**
  - O código gerado deve ser 100% compatível com as regras do **Ruff** (PEP 8, import sorting via `isort`, flakes).
  - Nomes de funções e variáveis em `snake_case`; classes em `PascalCase`; constantes em `UPPER_SNAKE_CASE`.

---

## 2. Arquitetura & Design de Software

- **Arquitetura em Camadas (Clean / Hexagonal):**
  - Mantenha a lógica de domínio e regras de negócio completamente desacopladas de adaptadores externos (HTTP, banco de dados, filas, SDKs de nuvem).
  - Utilize interfaces abstratas (`typing.Protocol` ou `abc.ABC`) para definir contratos de dependências externas.
- **Injeção de Dependências:**
  - Promova acoplamento fraco injetando dependências via construtores (`__init__`) ou frameworks injetores (ex: dependências nativas do FastAPI).
- **Tratamento de Exceções:**
  - Crie exceções customizadas para o domínio que herdem de uma exceção base do projeto.
  - Nunca capture exceções genéricas com `except Exception:` vazio; capture exceções específicas e sempre utilize `raise CustomError(...) from err` para preservar o stack trace original.

---

## 3. Concorrência & I/O Assíncrono

- Priorize `async/await` com `asyncio` para operações intensivas de rede e I/O (requisições HTTP via `httpx`, drivers de banco assíncronos como `asyncpg` ou `motor`).
- Nunca execute chamadas bloqueantes de I/O dentro do event loop assíncrono (utilize `asyncio.to_thread` se uma biblioteca externa for síncrona).

---

## 4. Segurança, Governança & LGPD

- **Segredos e Credenciais:** Nunca inclua chaves de API, senhas, tokens ou URLs de banco de dados hardcoded. Use injeção via variáveis de ambiente com Pydantic Settings.
- **Dados Sensíveis (PII / Masking):** Garanta que nenhum dado pessoal identificável, payload não sanitizado ou token seja impresso em logs.
- **Prevenção de Vulnerabilidades:**
  - Não utilize `eval()`, `exec()` ou `pickle` em dados de fontes não confiáveis.
  - Utilize queries parametrizadas (via SQLAlchemy / ORM / Drivers seguros) para evitar SQL Injection.

---

## 5. Observabilidade & Logs

- **Structured Logging:**
  - Utilize logs estruturados (JSON format) usando bibliotecas como `structlog` ou `loguru`.
  - Sempre inclua contexto nas mensagens de log (`correlation_id`, `tenant_id`, `operation`), evitando formatação de strings puras com print statements.
- **Níveis de Log:**
  - `DEBUG`: Apenas para diagnósticos detalhados em ambiente de desenvolvimento.
  - `INFO`: Acontecimentos relevantes do ciclo de vida da aplicação e fluxos de negócio concluídos.
  - `WARNING`: Falhas tratadas com fallback ou comportamentos anômalos.
  - `ERROR`: Falhas de execução que impedem o cumprimento da requisição/transação.

---

## 6. Testes Automatizados (Pytest)

- Escreva testes utilizando o framework **pytest**.
- **Padrão AAA (Arrange, Act, Assert):** Estruture cada função de teste de forma legível e modular.
- **Mocks & Fixtures:**
  - Utilize fixtures modulares no `conftest.py`.
  - Use `pytest-mock` para isolar chamadas de rede externas e banco de dados.
- **Testes Assíncronos:** Utilize o plugin `pytest-asyncio` (`@pytest.mark.asyncio`) para rotinas assíncronas.
- Garanta cobertura para caminhos felizes (*happy path*), cenários de borda (*edge cases*) e exceções esperadas (`pytest.raises`).