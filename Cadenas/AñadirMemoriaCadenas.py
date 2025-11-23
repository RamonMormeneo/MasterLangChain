# librerias 

from operator import itemgetter

from langchain_openai import ChatOpenAI

from langchain.memory import ConversationBufferMemory

from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain.schema import StrOutputParser

# cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# iniciamos el modelo de OpenAI

modelo = ChatOpenAI()

# definimos el prompt

prompt = ChatPromptTemplate.from_messages([('system', 'Eres un asistente.'),
                                           
                                           MessagesPlaceholder(variable_name='history'),
                                           
                                           ('human', '{pregunta}')
                                          ])

# parser de salida, transforma la salida a string

parser = StrOutputParser()

# definimos el objeto de memoria

memoria = ConversationBufferMemory(return_messages=True)

# iniciamos la memoria

memoria.load_memory_variables({})

# definimos la cadena

cadena = (RunnablePassthrough.assign(
          history=RunnableLambda(memoria.load_memory_variables) | itemgetter('history'))
         
          | prompt
         
          | modelo
          
          | parser
         )

# respuesta de la cadena

pregunta = {'pregunta': 'Hola, soy Pepe'}

respuesta = cadena.invoke(pregunta)

respuesta

# guarda la conversacion en la memoria

memoria.save_context(pregunta, {'respuesta': respuesta})

# memoria de la cadena

memoria.load_memory_variables({})

# segunda respuesta de la cadena

pregunta = {'pregunta': '¿como me llamo?'}

respuesta = cadena.invoke(pregunta)

respuesta