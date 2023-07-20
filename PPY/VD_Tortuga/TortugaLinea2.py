import turtle as tt

e = 5    #Espacio entre líneas
tm = 10  #Tamaño de la línea
n = 10   #Número de líneas a dibujar

#Dibuja la primera línea
for i in range(n):
    tt.forward(tm + i*2)
    tt.penup()       #Mueve la tortuga sin que esta dibuje su movimiento
    tt.forward(e)
    tt.pendown()     #Para que vuelva a dibujar

#Cierra la ventana cuando se hace click sobre la misma
tt.exitonclick()