from langchain.text_splitter import RecursiveCharacterTextSplitter

# importamos un archivo de texto

with open('../../../files/shakespeare.txt', 'r') as f:
    
    texto = f.read()

# nº de cararcteres del texto

len(texto)

splitter = RecursiveCharacterTextSplitter(chunk_size=100,        # tamaño del fragmento
                                          chunk_overlap=50,      # superposición
                                          length_function=len,   # funcion de longitud
                                          add_start_index=True,  # indice de inicio
                                         )

trozos = splitter.create_documents([texto])

trozos[0]


trozos[1]

#spliter por caracter

from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(separator='\n',           # caracter separador
                                 chunk_size=1000,          # tamaño del fragmento
                                 chunk_overlap=200,        # superposición
                                 length_function=len,      # funcion de longitud
                                 is_separator_regex=False, # regex o no
                                )

trozos = splitter.create_documents([texto])

trozos[0]

#spliter de html

from langchain.text_splitter import HTMLHeaderTextSplitter

# extraccion de html en texto

import requests as req

url = 'https://es.wikipedia.org/wiki/Python'

html = req.get(url=url).text

# nº de caracteres del texto

len(html)

# division por cabeceras

splitter = HTMLHeaderTextSplitter(headers_to_split_on= [('h1', 'Header 1'), ('h2', 'Header 2')])

trozos_html = splitter.split_text(html)

trozos_html[0]

#en combinacion con otros puedes hacer una manipulacion mas compleja

# trozos directamente desde la url

trozos_html = splitter.split_text_from_url(url)

splitter_recursivo = RecursiveCharacterTextSplitter(chunk_size=500)

trozos = splitter_recursivo.split_documents(trozos_html)

trozos[0]

#dividir codigo

from langchain.text_splitter import Language


# con codigo de python

python = '''
         def hello_world():
             print('Hello, World!')
         hello_world()
         '''
splitter = RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=200)

trozos = splitter.create_documents([python])

trozos[0]

# con codigo de javascript

js = '''
     function helloWorld() {
       console.log("Hello, World!");
     }
     helloWorld();
     '''

splitter = RecursiveCharacterTextSplitter.from_language(language=Language.JS, chunk_size=200)

trozos = splitter.create_documents([js])

trozos[0]

#token text spliter

from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(chunk_size=200)

trozos = splitter.split_text(texto[:100])

trozos[0]

#Long context split

from langchain.document_transformers import LongContextReorder

reorden = LongContextReorder()

trozos = reorden.transform_documents(trozos)

trozos[0]