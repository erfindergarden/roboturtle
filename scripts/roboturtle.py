from roboturtle.localturtle import LocalTurtle

WORLD_SCALE = 0.1

if __name__ == '__main__':

    import turtle
    from time import sleep

    screen = turtle.Screen()

    turtle = LocalTurtle()

    for el in range(2):
        turtle.forward(turtle)
        sleep(2)
        turtle.left(90)
        sleep(2)
        turtle.backward(turtle)
        sleep(2)
        turtle.right(180)
        sleep(2)

