import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the environment variables from the .env file
load_dotenv()

# Fetch individual configuration values
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Use your variables safely
# print(f"Google API Key: {GOOGLE_API_KEY}")

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

modelo_de_prompt = PromptTemplate(
    template=(
        "Me diga quais os impactos da IA no {assunto} e como ela pode ser usada "
        "para melhorar a produtividade."
    ),
    input_variables=["assunto"],
)

cadeia = modelo_de_prompt | llm | StrOutputParser()

resposta = cadeia.invoke({"assunto": "bancário"})
print(resposta)
