# primero cargamos la API KEY de OpenAI

from dotenv import load_dotenv 
import os

# carga de variables de entorno
load_dotenv()


# api key openai, nombre que tiene por defecto en LangChain
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#Calculo de circunferencias
from langchain.tools import BaseTool

from math import pi
from typing import Union


class Circunferencia(BaseTool):
    
    # atributos, se necesitan estos nombres de atributos y que esten tipados
    name: str = 'Calcula longitud de la circunferencia'
    
    description: str = 'Usa esta herramienta para calcular la circunferencia dado el radio'
        
    
    def _run(self, radio: Union[int, float]):
        """
        Método para calcular la longitud
        Necesita el nombre `_run` para poder ser ejecutada
        
        Params:
        radio: int o float, radio de la circunferencia
        
        Return:
        float con la longitud de la circunferencia
        """
        return  2.0 * pi * float(radio)
    
    
    
    def _arun(self, radio: Union[int, float]):
        """
        Método para ejecución asincrona.
        No implementado.
        """
        raise NotImplementedError('Esta herramienta no soporta async')
    
from langchain_openai import ChatOpenAI

# iniciamos el modelo LLM

llm = ChatOpenAI(temperature=0,                # temperatura a cero implica cero invencion
                 model_name='gpt-3.5-turbo'    # nombre del modelo
                )

# objeto de memoria del chat

from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# iniciamos la memoria del chat 

memoria_chat = ConversationBufferWindowMemory(memory_key='chat_history',
                                              k=5,
                                              return_messages=True)

# objeto para iniciar el agente

from langchain.agents import initialize_agent

# iniciamos el agente con la herramienta

agente = initialize_agent(tools=[Circunferencia()],
                          llm=llm,
                          memory=memoria_chat,
                          verbose=True
                         )
# uso del agente

agente.invoke('calcula la circunferencia de radio 7.81')

#agente duck duck

from langchain.tools import DuckDuckGoSearchRun

agente = initialize_agent(tools=[DuckDuckGoSearchRun()],
                          llm=llm,
                          memory=ConversationBufferWindowMemory(memory_key='chat_history'),
                          verbose=True
                         )

agente.invoke('año invencion bombilla')

#agente shelltool

from langchain.tools import ShellTool

agente = initialize_agent(tools=[ShellTool()],
                          llm=llm,
                          memory=ConversationBufferWindowMemory(memory_key='chat_history'),
                          verbose=True
                         )

agente.invoke('dime todos los archivos de esta carpeta')

#agente pandas

# importamos el agente predefinido

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# cargamos el dataframe

import pandas as pd

df = pd.read_csv('../../../files/airbnb.csv')

# informacion del dataframe

df.info()

# definimos el modelo 

from langchain_openai import OpenAI

llm = OpenAI(temperature=0)

# creamos el agente

agente = create_pandas_dataframe_agent(llm=llm, 
                                       df=df, 
                                       verbose=True, 
                                       allow_dangerous_code=True)

agente.invoke('¿cuantas filas tiene la tabla?')

len(df)

agente.invoke('¿cual es el precio medio?')

df['price'].mean()

#agente SQL

# importamos el agente y las herramientas

from langchain.agents import create_sql_agent

from langchain.agents.agent_toolkits import SQLDatabaseToolkit

from langchain.sql_database import SQLDatabase

# definimos la uri y la conexion a la base de datos

uri = 'mysql+pymysql://root:password@localhost:3306/publications'

db = SQLDatabase.from_uri(uri)

# herramienta de SQL

herramienta = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

# agente SQL

agente = create_sql_agent(llm=OpenAI(temperature=0),
                          toolkit=herramienta,
                          verbose=True)

agente.invoke('¿cuantos autores hay en la tabla?')

agente.invoke('¿cuantas ventas tiene cada tienda?')