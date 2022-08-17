print(2+3)
# 5

print(3-1)
# 2

print(7%3)
# 1 : 나머지 값

print(7//3)
# 2 : 몫 계산

print("강아지" + '고양이' + "\n햄스터")
# 강아지고양이
# \n : 기능은 줄 바꿈...
print("300" + "400")
# 300400 : 문자취급

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(30)

print('피자 ' *11)

# pront('피자')

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 1000:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5
