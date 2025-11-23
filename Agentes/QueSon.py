#Herramointas

#buscador de internet Duck Duck
from langchain.tools import DuckDuckGoSearchRun
buscador = DuckDuckGoSearchRun()
buscador.run('que es langchain')

from langchain_community.tools import DuckDuckGoSearchResults
buscador = DuckDuckGoSearchResults()

buscador.run('que es langchain')

#Shelltool ejecutar comandos

from langchain.tools import ShellTool
shell = ShellTool()

resultado = shell.run({'commands': ['ls', 'echo hola']})
resultado.split('\n')

#Youtube Search

from langchain.tools import YouTubeSearchTool

youtube = YouTubeSearchTool()
busqueda = 'Soil & Pimp Sessions'
youtube.run(busqueda)

busqueda = 'Soil & Pimp Sessions, 5'
youtube.run(busqueda)

#Wikipedia
from langchain.tools import WikipediaQueryRun

from langchain.utilities import WikipediaAPIWrapper
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

#Herramienta custom

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
    
# uso herramienta custom

Circunferencia().run(tool_input={'radio': 0.5})

#Lista de herramientas

from langchain.agents import Tool

# añadimos DuckDuckGo

herramientas = [Tool(name='DuckDuckGo',
                     func=buscador.run,
                     description='Utilidad de busqueda en internet')]

type(herramientas)

# añadimos wikipedia

herramientas.append(Tool(name='Wikipedia',
                         func=wikipedia.run,
                         description='Utilidad de busqueda en wikipedia'))

# añadimos youtube

herramientas.append(Tool(name='Youtube',
                         func=youtube.run,
                         description='Utilidad de busqueda en youtube'))