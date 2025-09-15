# modulu kodumuza import(daxil) edirik
import turtle

# shape(formasın) və speed(sürətin) qeyd edirik
turtle.shape("turtle")
turtle.speed(10)

# loop(döngə) yaradırıq, harda 36 kvadrat çəkiləcək
for i in range(36):
    # hər kvadratın 4 tərəfi olduğundan 4 dəfə təkrarlayırıq
    for j in range(4):
        turtle.forward(100) #100px qabağa
        turtle.left(90) #90 dərəcə sola
    turtle.left(10) #10 dərəcə sola

#kod anidən bağlanmasın deyə
input()