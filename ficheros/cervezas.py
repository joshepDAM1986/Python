from urllib import request
from urllib.error import URLError
from urllib.error import HTTPError

try:
    f = request.urlopen(
        "https://firebasestorage.googleapis.com/v0/b/chat-7d403.appspot.com/o/Cervezas.csv?alt=media&token=b285ec18-f95c-408d-a3a3-2dc6f3db10d7")
except HTTPError:
    print("Error de peticion HTTP")
except URLError:
    print("No existe la url")
else:
    contenido = f.read().decode("utf-8")
    # print(contenido)
    lineas=contenido.split("\r\n")
    print(lineas)
    f.close()