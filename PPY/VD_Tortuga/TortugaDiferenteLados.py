import turtle as tt

#Colocamos el cursor en la ventana
tt.penup()
tt.goto(-250, 0)
tt.pendown()

#Función que sirve para dibujar una figura de cualquier número de lados (> 2)
def draw_shapes(sides, length):
    for _ in range(sides):
        tt.forward(length)
        tt.left(360 / sides)

#Dibuja la primera figura
draw_shapes(3, 100)

#Desplazamos la totuga hacia la derecha
tt.penup()
tt.forward(100 * 1.5)
tt.pendown()

#Dibuja la segunda figura
draw_shapes(4, 100)

#Desplazamos la totuga hacia la derecha
tt.penup()
tt.forward(100 * 2)
tt.pendown()

#Dibuja la tercera figura
draw_shapes(5, 100)

#Cierra la ventana cuando se hace click sobre la misma
tt.exitonclick()