import turtle as tt

l = 100  #Longitud del lado del hexágono

def hexagono():
    for _ in range(6):
        tt.forward(l)
        tt.left(60)

hexagono()

#Cierra la ventana cuando se hace click sobre la misma
tt.exitonclick()