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

from langchain.utilities import SQLDatabase

from langchain.schema.runnable import RunnablePassthrough

from langchain.chains import create_tagging_chain

# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# esquema de etiquetas

esquema = {'properties': {'sentiment': {'type': 'string'},
                          'aggressiveness': {'type': 'integer'},
                          'language': {'type': 'string'}
                         }
          }

# creacion de la cadena

cadena = create_tagging_chain(llm=modelo, schema=esquema)

# respuesta cadena

texto = 'Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!'

cadena.invoke(texto)

# respuesta cadena

texto = 'Estoy muy enojado contigo! Te voy a dar tu merecido!'

cadena.invoke(texto)