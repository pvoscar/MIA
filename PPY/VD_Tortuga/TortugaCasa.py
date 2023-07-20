import turtle as tt
import math

l = 150  #Longitud del lado de la casa
h = math.sqrt(l**2 + l**2)

#Dibuja la diagonal principal de la casa (derecha)
tt.left(45)
tt.forward(h)
#Dibuja el lado superior de la casa
tt.left(135)
tt.forward(l)
#Dibuja la diagonal principal de la casa (izquierda)
tt.left(135)
tt.forward(h)
#Dibuja el lado derecho de la casa
tt.left(135)
tt.forward(l)
#Dibuja el techo de la casa (lado izquierdo)
tt.left(45)
tt.forward(h/2)
#Dibuja el techo de la casa (lado derecho)
tt.left(90)
tt.forward(h/2)
#Dibuja el lado izquierdo de la casa
tt.left(45)
tt.forward(l)
#Dibuja la base de la casa
tt.left(90)
tt.forward(l)

#Cuando se presiona en la pantalla se cierra
tt.exitonclick()