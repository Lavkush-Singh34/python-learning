import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

# t = turtle.Turtle()
# t.speed(0)
# t.left(90)
#
# def tree(length):
#     if length < 5:
#         return
#
#     t.forward(length)
#
#     t.left(30)
#     tree(length * 0.7)
#
#     t.right(60)
#     tree(length * 0.7)
#
#     t.left(30)
#     t.backward(length)
#
# tree(150)
#
# turtle.done()


# t = turtle.Turtle()
# t.speed(0)
# turtle.tracer(False)
#
#
# def koch(n):
#     if n < 3:
#         t.forward(n)
#         return
#
#     n /= 3
#
#     koch(n)
#     t.left(60)
#     koch(n)
#     t.right(120)
#     koch(n)
#     t.left(60)
#     koch(n)
#
#
# for _ in range(3):
#     koch(300)
#     t.right(120)
#
# turtle.done()

## Best and easy

t = turtle.Turtle()
t.speed(3)

turtle.tracer(False)
for i in range(1720):
    t.forward(i * 0.5)
    t.left(91)

turtle.done()


# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("black")
#
# for i in range(360):
#     t.pencolor(["red", "cyan", "yellow", "lime", "magenta", "orange"][i % 6])
#
#     t.circle(200)
#     t.left(1)
#
# turtle.done()


# t = turtle.Turtle()
# t.speed(0)
#
# scale_x = 2
# scale_y = 100
#
# t.penup()
#
# for x in range(-360, 361):
#     y = math.sin(math.radians(x)) * scale_y
#
#     if x == -360:
#         t.goto(x * scale_x, y)
#         t.pendown()
#     else:
#         t.goto(x * scale_x, y)
#
# turtle.update()
# turtle.done()
#
#
