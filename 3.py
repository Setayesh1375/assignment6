import math

def darage_3(a,b,c,d):
    delta0 = (b**2) - (3*a**3)
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d

    u1 = 1
    u2 = complex(-1, math.sqrt(3)) * 0.5
    u3 = complex(-1, -math.sqrt(3)) * 0.5

    C = ((delta1 + math.sqrt(delta1**2 - 4*delta0**3))/2)**(1/3)
    
    x1 = (-1/(3*a)) * (b + u1*C + delta0/(u1*C))
    x2 = (-1/(3*a)) * (b + u2*C + delta0/(u2*C))
    x3 = (-1/(3*a)) * (b + u3*C + delta0/(u3*C))
    
    print (x1, x2, x3)


s1 = input("zarib X be tavan 3 : ")
s2 =  input("zarib X be tavan 2 : ")
s3 = input("zarib X be tavan 1 : ")
s4 = input("zarib X be tavan 0 : ")

darage_3(s1,s2,s3,s4)