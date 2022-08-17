# 변수를 사용하는 이유
x = 100
y = 200
sum = x + y
times = x * y
print(x, '와', y, '의 합:', sum, ', 곱:', times)    # 같은 결과
print(f'{x} 와 {y} 의 합: {sum} , 곱: {times}')     # 같은 결과
print(f'{x} 와 {y} 의 합: {x+y} , 곱: {x*y}')       # 같은 결과
print(f'{x} 와 {y} 의 차: {y-x} , 나눗셈: {y/x}')     

import turtle
import time
t = turtle.Turtle()
t.shape("turtle")
r = int(input('원의 반지름을 입력하세요.(1 ~ 100) : '))
c = input('원의 색을 입력하세요.(blue,red,green,yellow) : ')
t.color(c)
t.begin_fill()
t.circle(r)
t.end_fill()
time.sleep(5)