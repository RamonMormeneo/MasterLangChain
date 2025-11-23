#buscador de internet

# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos librerias

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate

from langchain.schema.output_parser import StrOutputParser

from langchain.tools import DuckDuckGoSearchRun

# definimos la herramienta, buscador de DuckDuckGo

buscador = DuckDuckGoSearchRun()

# plantilla de texto para el prompt

plantilla = '''Convierte la siguiente pregunta en una 
               consulta de búsqueda para un motor de búsqueda:
               
               {pregunta}'''

# creamos el prompt

prompt = ChatPromptTemplate.from_template(plantilla)

# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# creamos la cadena

cadena = prompt | modelo | parser | buscador

# respuesta de la cadena

respuesta = cadena.invoke({'pregunta': 'Me gustaría saber qué partidos hay esta noche.'})
