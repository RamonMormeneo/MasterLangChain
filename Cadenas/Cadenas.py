# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# preparamos el prompt

from langchain.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    
    ('system', '''Eres un historiador muy erudito que ofrece respuestas precisas y 
                  elocuentes a preguntas históricas y que responde en castellano.'''),
    
    ('human', '{pregunta}')
    
])
# iniciamos el modelo llm

from langchain_openai import ChatOpenAI

modelo = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

# parser de salida, transforma la salida a string

from langchain.schema import StrOutputParser

parser = StrOutputParser()

# creamos la cadena con lcel

cadena = prompt | modelo | parser

# llamada a la cadena

pregunta = '¿Cuales son las 7 maravillas del mundo?'

respuesta = cadena.invoke({'pregunta': pregunta})
respuesta.split('\n')

# podemos hacer la llamada a la cadena para que sea por chunks

pregunta = '¿Cuales fueron las conquistas de Alejandro de Macedonia?'

for chunk in cadena.stream({'pregunta': pregunta}):

    print(chunk, end='', flush=True)