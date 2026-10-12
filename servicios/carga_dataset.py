from rich.console import Console #Es sólo para darle estilo al print
import json #importamos el módulo json para poder cargar el dataset de mangas
console = Console()#Es sólo para darle estilo al print


with open('datos/dataset_mangas_10.json', 'r', encoding='utf-8') as mangas: 
    # Usamos "open" para abrir el archivo"
    # La "r" es porque sólo vamos a leer
    # La codificación "utf-8" la usamos para manejar caracteres especiales como acentos y eñes
    catalogo = json.load(mangas) # Carga el contenido en un diccionario o lista

    
for item in catalogo["mangas"]: # Accedemos a la lista que está dentro de la clave "mangas" del dataset.
    console.print("[bold cyan]Nombre del manga:[/bold cyan]", item["nombre"]) #
    #Rich cambia "Nombre del manga" a color cyan y en negrita usando "console.print" y [bold cyan]texto[/bold cyan].


console.print("LISTA COMPLETA:",catalogo, style="bold red") #Imprime todo la lista o diccionario


