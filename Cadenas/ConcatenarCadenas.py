#Cadena simple
# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# librerias

from langchain.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI

from langchain.schema import StrOutputParser

# preparamos el prompt

prompt = ChatPromptTemplate.from_messages([
    
    ('system', '''Eres un historiador muy erudito que ofrece respuestas precisas y 
                  elocuentes a preguntas históricas y que responde en castellano.'''),
    
    ('human', '{pregunta}')
    
])
# iniciamos el modelo llm

modelo = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# creamos la cadena con lcel

cadena = prompt | modelo | parser

# llamada a la cadena

pregunta = '¿Cuales son las 7 maravillas del mundo?'

respuesta = cadena.invoke({'pregunta': pregunta})

respuesta.split('\n')


#concatenar cadenas


# creamos la plantilla de traducción con la respuesta de la cadena y el lenguaje de salida

prompt_traductor = ChatPromptTemplate.from_template('Translate {respuesta} to {lenguaje}')

# creamos la nueva cadena basada en la anterior a la cual le damos el lenguaje al que queremos traducir

cadena_traducida = (
    
    {'respuesta': cadena, 'lenguaje': lambda x: x['lenguaje']} 
    
    | prompt_traductor 
    
    | modelo 
    
    | parser
)

# respuesta de la doble cadena

respuesta = cadena_traducida.invoke({'pregunta': pregunta,
                                     'lenguaje': 'English'})

respuesta.split('\n')

# cambio de idioma

respuesta = cadena_traducida.invoke({'pregunta': pregunta,
                                     'lenguaje': 'Japanese'})

respuesta.split('\n')