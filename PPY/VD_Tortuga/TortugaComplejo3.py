import turtle as tt
import math

x = -2 * (math.pi)
A = 100
b = 100
c = 0
d = 0
period = (2 * (math.pi)/b)
y = A * (math.sin((period * x - c) + d))
tt.penup()
tt.goto(x, y)
tt.pendown()
x = (-23 * (math.pi)/12)
while x != 2 * (math.pi):
    y = A * (math.sin((period * x - c) + d))
    tt.goto(x, y)
    x = x + ((math.pi) / 12)