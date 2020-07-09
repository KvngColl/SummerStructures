import turtle
def draw_star(x, y):
    

    for i in range(5):
        turtle.forward(x)
        turtle.left(y)
        turtle.forward(x)
        turtle.left(72 - y)
    turtle.end_fill()
    return

draw_star(100, 144)
