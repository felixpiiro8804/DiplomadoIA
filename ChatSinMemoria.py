import os
import warnings
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

warnings.filterwarnings("ignore")

# 🔐 Cargar variables desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")

# 🤖 Configuración del modelo OpenRouter
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    model_name="cohere/north-mini-code:free",
    temperature=0.5,
)

print("💬 Chatbot vía OpenRouter (sin memoria) (escribe 'salir' para terminar)\n")

Meta_prompt = """

"""

while True:
    user_input = input("👤 Tú: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break

    try:
        # Cada consulta es independiente (sin memoria)
        prompt = f"""
Condiciones:
{Meta_prompt}

Usuario:
{user_input}
"""

        response = llm.invoke([HumanMessage(content=prompt)])

        if hasattr(response, "content"):
            print(f"🤖 Bot: {response.content.strip()}\n")

        elif isinstance(response, dict) and "content" in response:
            print(f"🤖 Bot: {response['content'].strip()}\n")

        elif isinstance(response, list) and len(response) > 0:
            print(f"🤖 Bot: {response[0].content.strip()}\n")

        else:
            print(f"🤖 Bot: {response}\n")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Error: {e}\n")