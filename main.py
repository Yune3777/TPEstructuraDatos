from servicios.catalogo import Catalogo
from ui.terminal import Terminal

def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/canciones_90s_10.json")
    
    terminal = Terminal(catalogo)
    terminal.iniciar()

if __name__ == "__main__":
    main()


    