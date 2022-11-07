import turtle
import random
t=turtle.Turtle()
t.speed(100)
length=1
for i in range(360):
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  t.color(r,g,b)
  t.forward(length)
  t.backward(length)
  t.right(5)
  length=length+1
  
