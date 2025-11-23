#conversation buffer

# quito warnings 

import warnings
warnings.filterwarnings('ignore')

# importamos el objeto de memoria

from langchain.memory import ConversationBufferMemory

# memoria con salida de string

memoria = ConversationBufferMemory()

# guardado de mensajes

mensaje_usuario = {'input': 'hola'}


mensaje_asistente = {'output': 'hola, ¿como estás?'}


memoria.save_context(mensaje_usuario, mensaje_asistente)

# lectura de mensajes

memoria.load_memory_variables({})

# memoria con salida de lista de mensajes

memoria = ConversationBufferMemory(return_messages=True)

# guardado de mensajes

mensaje_usuario = {'input': 'hola'}


mensaje_asistente = {'output': 'hola, ¿como estás?'}


memoria.save_context(mensaje_usuario, mensaje_asistente)

# lectura de mensajes

memoria.load_memory_variables({})


# memoria con salida de lista de mensajes y cambio de key

memoria = ConversationBufferMemory(return_messages=True, memory_key='historial')

# guardado de mensajes

mensaje_usuario = {'input': 'hola'}


mensaje_asistente = {'output': 'hola, ¿como estás?'}


memoria.save_context(mensaje_usuario, mensaje_asistente)

# lectura de mensajes

memoria.load_memory_variables({})

#Conversation buffer window, lista de interaciones reciente y/o las ultimas K intertaciones

# importamos el objeto de memoria

from langchain.memory import ConversationBufferWindowMemory

# memoria que solo recuerda el ultimo dialogo

memoria = ConversationBufferWindowMemory(k=1, 
                                         return_messages=True,
                                         memory_key='historial'
                                         )

# guardado de los primeros mensajes 

mensaje_usuario = {'input': 'hola'}

mensaje_asistente = {'output': 'hola, ¿como estás?'}

memoria.save_context(mensaje_usuario, mensaje_asistente)

# guardado de los segundos mensajes 

mensaje_usuario = {'input': 'yo bien, ¿y tú?'}

mensaje_asistente = {'output': 'estoy bien, gracias'}

memoria.save_context(mensaje_usuario, mensaje_asistente)

# lectura de mensajes

memoria.load_memory_variables({})

#Conversation Entity Memory, recordar hechos especificos usando LLM

# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# importamos memoria y llm

from langchain.memory import ConversationEntityMemory
from langchain_openai import OpenAI

# se define el llm

llm = OpenAI()

# memoria con entidad 

memoria = ConversationEntityMemory(llm=llm)

# guardado de los primeros mensajes 

mensaje_usuario = {'input': 'Pepe y Maria estan trabajando en un proyecto.'}

memoria.load_memory_variables(mensaje_usuario)

mensaje_asistente = {'output': 'Genial, ¿que tipo de proyecto?'}

memoria.save_context(mensaje_usuario, mensaje_asistente)

memoria.load_memory_variables({'input': 'quien es Pepe?'})

#Conversaton Knowledge Graph Memory, parecido a la anterior pero usando un grafo de conocimiento

# importamos memoria y llm

from langchain.memory import ConversationKGMemory

from langchain_openai import OpenAI

# se define el llm

llm = OpenAI()

# memoria con entidad 

memoria = ConversationKGMemory(llm=llm)

# uso de la memoria

memoria.save_context({'input': 'di hola a Pepe'}, {'output': '¿quien es Pepe?'})

memoria.save_context({'input': 'Pepe es un amigo'}, {'output': 'vale'})

memoria.load_memory_variables({'input': '¿quien es Pepe?'})

#Conversation Summary Memory, nos genera un resumen de la conversacion

# importamos memoria y llm

from langchain.memory import ConversationSummaryMemory

from langchain_openai import OpenAI

# se define el llm

llm = OpenAI()

# memoria de resumen

memoria = ConversationSummaryMemory(llm=llm)

# uso de la memoria

memoria.save_context({'input': 'di hola a Pepe'}, {'output': '¿quien es Pepe?'})

memoria.save_context({'input': 'Pepe es un amigo'}, {'output': 'vale'})

memoria.load_memory_variables({})

#Conversation Summary Buffer Memory, nos genera un resumen de la conversacion pero poniendo unos limites

# importamos memoria y llm

from langchain.memory import ConversationSummaryBufferMemory

from langchain_openai import OpenAI

# se define el llm

llm = OpenAI()

# memoria 

memoria = ConversationSummaryBufferMemory(llm=llm, max_token_limit=10)

# uso de la memoria

memoria.save_context({'input': 'di hola a Pepe'}, {'output': '¿quien es Pepe?'})

memoria.save_context({'input': 'Pepe es un amigo'}, {'output': 'vale'})

memoria.load_memory_variables({})

#COnversation Token Buffer Memeory, este se centra en la cantidad de interaciones y utiliza la longitud de tokens para determinar cuando vaicar
# importamos memoria y llm

from langchain.memory import ConversationTokenBufferMemory

from langchain_openai import OpenAI

# se define el llm

llm = OpenAI()

# memoria 

memoria = ConversationTokenBufferMemory(llm=llm, max_token_limit=10)

# uso de la memoria

memoria.save_context({'input': 'di hola a Pepe'}, {'output': '¿quien es Pepe?'})

memoria.save_context({'input': 'Pepe es un amigo'}, {'output': 'vale'})

memoria.load_memory_variables({})