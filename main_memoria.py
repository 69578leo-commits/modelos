# Contenido para: main_memoria.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory 
from dotenv import load_dotenv
import os

#
# === 1. LA FUNCIÓN (ESTO ESTÁ BIEN) ===
#
def crear_modelo_chat_limitado():
    """
    Crea un chain de conversación que solo recuerda
    los últimos 5 PARES de interacciones (k=5).
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("La variable GOOGLE_API_KEY no está definida en el archivo .env")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        google_api_key=api_key
    )

    #
    # === 2. LA MEMORIA (k=5) (ESTO ESTÁ BIEN) ===
    # k=5 son 5 PARES (5 tuyos, 5 de IA)
    #
    memory = ConversationBufferWindowMemory(k=5)

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True 
    )
    return conversation


#
# === 3. EL BLOQUE DE PRUEBA (AQUÍ ESTÁ LA CORRECCIÓN) ===
#
if __name__ == '__main__':
    print("Probando el modelo de 'Chat Limitado (k=5)'...")
    
    chain_de_prueba = crear_modelo_chat_limitado()
    
    print("Chat con Gemini (Límite 5 PARES). Escribe 'salir' para terminar.\n")
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ["salir", "exit"]:
            break

        #
        # ¡¡¡ESTA ES LA LÍNEA QUE ARREGLA TODO!!!
        # Usamos .invoke() que SÍ maneja la memoria.
        #
        respuesta_dict = chain_de_prueba.invoke({"input": mensaje})
        
        #
        # .invoke() devuelve un diccionario, 
        # la respuesta está en la clave 'response'
        #
        print("Gemini:", respuesta_dict.get('response', 'Error: No hubo respuesta'))