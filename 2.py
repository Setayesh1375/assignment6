
import turtle
p = turtle.Pen()
s=10
n = 3

while n < 100:
    i=360/n
    for j in range (n):
        p.forward (s+j)
        p.left (i)
        j+=1
   
    p.forward (s+j)
    p.left (i)
    n+=1
    s+=5  
turtle.done()
