rutaArch = "./Archivos/EjemploArchivo.txt"

file = open(rutaArch, "w")
file.write("Este es el contenido del archivo. \n")
file.close()

lista = ["Fresa", "Mango", "Papaya"]

with open(rutaArch, "a") as file:
    for e in lista:
        file.write(e + "\n")
        
print("Lista escrita en el archivo.")

lista2 = ["Honda ", "Suzuki ", "BMW "]
with open(rutaArch, "a") as file:
    file.writelines(lista2)
    
print("Lista escrita con writelines.")

print("Imprimir todo el contenido del archivo.")
with open(rutaArch, "r") as file:
    print(file.read())

print("Leer dos líneas y posteriormente 5 caracteres.")
with open(rutaArch, "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Almacenas el contenido en una lista y mostrar el último")
with open(rutaArch, "r") as file:
    contenido = file.readlines()
    print(contenido[-1])

