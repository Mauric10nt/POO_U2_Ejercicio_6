from ClaseManejadorViajerosFrecuentes import ManejadorViajerosFrecuentes
from ClaseViajeroFrecuente import ViajeroFrecuente
from claseMenu import Menu


if __name__ == "__main__":
    unManejadorViajeros = ManejadorViajerosFrecuentes()
    unManejadorViajeros.leer("viajeros.csv")

    unMenu = Menu()

    opcion = "0"

    unMenu.ejecutar(unManejadorViajeros)
