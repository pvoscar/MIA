def nuevoTema(tema):
    print("\n----------", tema, "----------\n")

if __name__ == "__main__":  #Se ejecuta solo si es el argumento prinicpal llamado por el intérprete

    print("-------------- Operadores Aritméticos -------------")
    print("Operador suma, 5 + 3 = ", 5 + 2)
    print("Operador resta 10 - 2 = ", 10 -2)
    print("Operador muktiplicación 3 * 3 = ", 3 * 3)
    print("Operador división 20 / 3 = ", 20 / 3)
    print("Operador división entera 20 // 3 = ", 20 // 3)
    print("Operador módulo 20 % 3 = ", 20 % 3)
    print("Operador cambio de signo -3 ", -3)
    print("Operador exponente 5 ** 5 = ", 5 ** 5)

    #Este es un comentario de una línea
    '''
        Este es un comentario de varias
        líneas
    '''
    print("\n-------------- Operadores Lógicos -------------\n")
    print("True and True: ", True and True) #Operador lógico and.

    #Actividad Imprimir la tabla de verdad del and
    print("\n-------------- Tabla de verdad (AND) -------------\n")
    print("True  and True: ",  True and True)
    print("True  and False: ", True and False)
    print("False and True: ",  False and True)
    print("False and False: ", False and False)

    #Actividad Imprimir la tabla de verdad del OR
    print("\n-------------- Tabla de verdad (OR) -------------\n")
    print("True  or True: ",  True or True)
    print("True  or False: ", True or False)
    print("False or True: ",  False or True)
    print("False or False: ", False or False)

    #Actividad Imprimir la tabla de verdad del NOT
    print("\n-------------- Tabla de verdad (NOT) -------------\n")
    print("not True: ",  not True)
    print("not False: ", not False)

    print("\n-------------- Operadores de comparación -------------\n")
    print("5 > 2:   ", 5 > 2)
    print("5 >= 10: ", 5 >= 10)
    print("3 < 10:  ", 3 < 10)
    print("5 <= 2:  ", 5 <= 2)
    print("5 == 5:  ", 5 == 5)
    print("7 != 20: ", 7 != 20)

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3 = "Pepe"
    nombreVariable = 8
    nombre_variable = 34.2
    print(variable1, _variable2, Variable3, nombreVariable, nombre_variable)

    a, b, c = 5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)

    nuevoTema("Enteros")
    w = 105
    x = 78658965235632
    y = -256
    z = 0b00110011

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Flotantes")
    x = 1234.56
    print(x, type(x))
    y = -9874.56
    print(y, type(y))

    nuevoTema("Números complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Booleanos")
    lis = []
    print(lis, "is", bool(lis))
    t = ()
    print(t, "is", bool(t))
    new = 'Hello'
    print(new, "is", bool(new))
    num = 99
    print(num, "is", bool(num))
    comp = 0 + 0j
    print(comp, "is", bool(comp))
    val = None
    print(val, "is", bool(val))

    nuevoTema("Listas")
    a = [10, 20.5, "Python List"]
    print(a)
    print(a[1])
    a[1] = "hola"
    print(a)

    nuevoTema("Tuplas")
    t  = (25, 'tuple', 1 + 10j)
    print(t)
    print("t[1] = ", t[1])
    print("t[0:3] = ", t[0:3])
    # t[1] = "Hola"  #Operación no válida en tuplas.
    # print(t)

    nuevoTema("Cadenas")
    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto también es una cadena'
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena1[5])

    cadenaMultilinea = '''Esto es una cadena
    de varias líenas    con     tabulares y
    saltos
    de 
    linea'''
    print(cadenaMultilinea, type(cadenaMultilinea))

    cadena3 = "Hola" * 5
    print(cadena3)

    nuevoTema("Conjuntos")
    conjunto = {10, 20, 30, 40, 10, 50}
    print("conjunto = ", conjunto)
    print(type(conjunto))

    nuevoTema("Diccionarios")
    diccionario = {"Nombre": "Conrado",
                "Edad": 38,
                "Tel": 1234567890}
    print(diccionario)
    print(diccionario["Nombre"])
    print(diccionario["Edad"])
    print(diccionario["Tel"])

