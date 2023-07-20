import turtle as tt

lh = 200  #Longitud horizontal del rectángulo
lv = 100   #Longitud vertical del rectángulo

for _ in range(2):
    tt.forward(lh)
    tt.left(90)
    tt.forward(lv)
    tt.left(90)

#Cierra la ventana cuando se hace click sobre la misma
tt.exitonclick()