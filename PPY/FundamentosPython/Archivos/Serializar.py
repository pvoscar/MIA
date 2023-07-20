#import sys
#sys.path.append('/Users/oscarluispenavalerio/Library/CloudStorage/GoogleDrive-olpenav@itsav.edu.mx/Mi unidad/U-ALINNCO/Materias Semestre 1/1. Programacion Python/MIA_Python/')

#from FundamentosPython import nuevoTema

import pickle

if __name__ == "__main__":
    #nuevoTema("Módulo Pickle y serialización binaria.")
    print("\n-------------- Módulo Pickle y serialización binaria ---------------\n")

    info = [35, 88, 3.14, 16]

    rutaArch = "./Archivos/ArchivoSerial"

    with open(rutaArch, "wb") as binFile:
        pickle.dump(info, binFile)

    print("Archivo binario escrito")

    with open(rutaArch, "rb") as binFile:
        lista = pickle.load(binFile)
        print(lista)

