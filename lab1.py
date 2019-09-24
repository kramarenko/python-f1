import turtle

turtle.shape('turtle')
width = 50
side = 3
step = 150
plus = 10


def figure(width, side=3, plus=10):
    angle = 360 / side;
    w = width;

    for x in range(side):
        turtle.forward(w)
        turtle.left(angle)
        print("x", x)
        if (x == side - 1):
            turtle.right(angle)
            turtle.penup()
            turtle.forward(15)
            turtle.left(angle)
            turtle.pendown()


for x in range(3, 12):
    figure(width + 25 * 2, x)
