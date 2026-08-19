import os

import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Fetch individual configuration values
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# 1. Ferramentas reais do agente
def somar_numeros(a: float, b: float) -> float:
    """Soma dois números."""
    print(f"Soma de {a} e {b}...")
    return a + b


def subtrair_numeros(a: float, b: float) -> float:
    """Subtrai dois números."""
    print(f"Subtração de {a} e {b}...")
    return a - b


def consultar_saldo(cliente_id: str) -> str:
    """Consulta o saldo bancário de um cliente."""
    print(f"Consultando saldo do cliente {cliente_id}...")
    return f"Saldo do cliente {cliente_id}: R$ 5.420,00"


# 2. Configura o modelo com as ferramentas nativas (Function Calling)
genai.configure(api_key=GOOGLE_API_KEY)  # type: ignore[attr-defined]
modelo = genai.GenerativeModel(  # type: ignore[attr-defined]
    model_name="gemini-3-flash-preview", tools=[somar_numeros, subtrair_numeros, consultar_saldo]
)

# 3. O "Loop Agêntico" nativo
chat = modelo.start_chat(enable_automatic_function_calling=True)

# O agente decide sozinho se precisa chamar a função, executa em Python e responde
resposta = chat.send_message(
    "Qual o saldo do cliente 123 e quanto ele terá se eu subtrair 300 reais?"
)

print(resposta.text)
