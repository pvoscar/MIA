import turtle as tt

l = 100  #Longitud del lado del cuadrado
n = 3    #Número de veces en que se repite el cuadrado

tt.left(20) #Movemos la tortuga 20º a la izquierda
for _ in range(n):  #Para repetir el número de cuadrados
    for _ in range(4):  #Para dibujar un cuadrado
        tt.forward(l)
        tt.left(90)
    #Mover el cuadrado cierto grado    
    tt.left(20)

tt.exitonclick()