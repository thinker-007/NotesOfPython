import turtle as T
from random import randint, random
from time import sleep

# 画樱花的�?�?(60,t)
def Tree(branch, t):
    sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if  randint(0, 2) == 0:
                t.color('snow')  # �?
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 3)
        elif branch < 8:
            if  randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 淡珊瑚色
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # �?(zhě)�?
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 *random()
        t.right(20 * a)
        b = 1.5 *random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花�?
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 *random()
        b = 10 - 20 *random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 淡珊瑚色
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat小麦
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的�?�?
Tree(60, t)
# 掉落的花�?
Petal(200, t)
w.exitonclick()