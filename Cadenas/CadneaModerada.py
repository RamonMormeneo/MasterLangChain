# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos librerias

from langchain_openai import OpenAI

from langchain.chains import OpenAIModerationChain

from langchain.prompts import ChatPromptTemplate

# modelo de moderacion

moderacion = OpenAIModerationChain()

# iniciamos el modelo de OpenAI

modelo = OpenAI()

# creamos el prompt

prompt = ChatPromptTemplate.from_messages([('system', 'repeat after me: {input}')])

# definimos la cadena

cadena = prompt | modelo

# respuesta de la cadena

cadena.invoke({'input': 'you are stupid'})

# definimos la cadena con moderacion

cadena_moderada = cadena | moderacion

# respuesta de la cadena moderada

cadena_moderada.invoke({'input': 'you are stupid'})['output']