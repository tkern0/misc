import turtle

ninja = turtle.Turtle()

ninja.speed(0)
x=0
for i in range(150):
    ninja.forward(100+i)
    ninja.right(170+i)
    ninja.forward(20+i)
    ninja.left(3*i)
    ninja.forward(50+i)
    ninja.right(30+i)
    ninja.forward(2*i-i)
    ninja.right(1.1**(1+i/10))

    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()
    ninja.color(["red", "chartreuse1", "DarkGoldenrod4", "gray53", "DeepSkyBlue1", "yellow2", "DarkOrchid2", "goldenrod2", "GreenYellow", "LavenderBlush","green2", "LightCyan4", "moccasin", "PapayaWhip"][i%14])
    ninja.right(2+i)

turtle.done()