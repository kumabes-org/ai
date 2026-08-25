import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain.agents import create_agent

# Load the environment variables from the .env file
load_dotenv()

# Fetch individual configuration values
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


@tool
def busca_web(query: str) -> list:
    """Busca na web por um termo específico"""            
    # Option A: Use the native tool directly
    #tavily_tool = TavilySearchResults(
    #    max_results=2,
    #    search_depth="advanced",
    #    max_tokens=1000
    #)
    # Instanciação da ferramenta
    tavily_tool = TavilySearch(max_results=2, search_depth="advanced")
    resultado_busca = tavily_tool.invoke(query)
    return resultado_busca


tools = [busca_web]


llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
llm_com_ferramenta = llm.bind(tools=tools)

# Instrução de sistema passada via parâmetro `prompt`
system_prompt = (
    "Você é um assistente especializado. "
    "Sempre utilize a ferramenta de busca_web para embasar sua resposta e inclua links de referência."
)

agente = create_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

# Execução
assunto = "bancário"
resposta = agente.invoke({
    "messages": [("user", f"Quais os impactos da IA no setor {assunto}?")]
})

# Exibe a resposta final do agente
print(resposta["messages"][-1].content)