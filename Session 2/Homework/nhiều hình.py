from turtle import *
n = int(input())
for i in range(3, n+1):
    for j in range(i):
        forward(100)
        color("red")
        left(360/i)
        color("blue")

        

        


mainloop()

