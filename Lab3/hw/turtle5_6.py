from turtle import *

def draw_star(x, y, length):
    up()
    goto(x, y)
    down()
    for i in range(5):
        right(144)
        forward(length)

speed(0)
color('black')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()