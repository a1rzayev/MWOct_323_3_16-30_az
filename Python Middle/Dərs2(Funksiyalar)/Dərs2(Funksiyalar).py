# modulları kodumuza import(daxil) edirik
import turtle 
import math



# shape(formasın) və speed(sürətin) qeyd edirik
turtle.shape("turtle")
turtle.speed(10)



# kvadrat çəkən funksiya
def draw_rectangle(size:float):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

# üçbucaq çəkən funksiya
def draw_triangle(size:float):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

# dairə çəkən funksiya
def draw_circle(radius:float):
    x = (2 * math.pi * radius) / 360
    for i in range(360):
        turtle.forward(x)
        turtle.left(1)



# kvadrat çəkən funksiya çağırırıq
draw_rectangle(200)

# üçbucaq çəkən funksiya çağırırıq
draw_triangle(200)

# dairə çəkən funksiya çağırırıq
draw_circle(200)