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

# # import turtle library
# colors = [ "red","purple","blue","green","orange","yellow"]
# my_pen = turtle.Pen()
# turtle.bgcolor("black")
# for x in range(360):
#    my_pen.pencolor(colors[x % 6])
#    my_pen.width(x/100 + 1)
#    my_pen.forward(x)
#    my_pen.left(59)