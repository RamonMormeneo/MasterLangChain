import warnings
warnings.filterwarnings('ignore')

from langchain.document_loaders import TextLoader

# cargamos el archivo de texto

loader = TextLoader('../../../files/shakespeare.txt')

# generamos el documento

documento = loader.load()

# devuelve una lista con un solo elemento, esta todo el texto en un solo objeto

type(documento)

len(documento)

type(documento[0])

#cvsloader
from langchain.document_loaders.csv_loader import CSVLoader

# cargamos el archivo csv

loader = CSVLoader('../../../files/airbnb.csv')

# generamos el documento

documento = loader.load()

# devuelve una lista con tantos elementos como filas tiene el archivo csv

type(documento)

len(documento)

# primera fila de la tabla

documento[0]

#carga de pdf

# ruta al archivo PDF

ruta_pdf = '../../../files/Matematicas_Basicas2023.pdf'

from langchain.document_loaders import PyPDFLoader

# cargamos el archivo

loader = PyPDFLoader(ruta_pdf)

# generamos el documento pagina a pagina

paginas = loader.load_and_split()

# nº de paginas

len(paginas)

# primera pagina

paginas[0]

from langchain.document_loaders import PyMuPDFLoader
# cargamos el archivo

loader = PyMuPDFLoader(ruta_pdf)

# generamos el documento

paginas = loader.load()

len(paginas)

from langchain.document_loaders import PDFMinerLoader

# cargamos el archivo

loader = PDFMinerLoader(ruta_pdf)

# generamos el documento

paginas = loader.load_and_split()

len(paginas)

#Youtube

from langchain.document_loaders import YoutubeLoader

url = 'https://www.youtube.com/watch?v=SMtWvDbfHLo'

loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)

loader.load()