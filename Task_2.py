"""1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
на квадраты с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов
и кол-во полученных квадратов."""
#"""2. Графически изобразите результат нарезки прямоугольника на квадраты: создайте двумерный массив символов
# размером a на b, заполните его символами кодировки base64, соответствующими номерам квадратов.
#Если квадратов больше 64, используйте символы повторно по кругу. Выведите заполненный двумерный массив."""
def squares(a, b, c):
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
    c = random.choice(colors)
    if a == b:
        kol_vo=1
        print ("длины сторон {} ".format(a))
    else:
        if a > b:
            kol_vo=1 + squares(a - b, b,c)
            print("длины сторон {} ".format(b))
            plot([a-b,a-b], [0,b], c)

        else:
            kol_vo=1 + squares(a, b - a,c)
            print("длины сторон {}".format(a))
            plot([a, 0], [b-a, b-a], c)
    return(kol_vo)

from matplotlib.pyplot import *
import random

a=int(input("Введите a - сторону прямоугольника:\n"))
b=int(input("Введите b - сторону прямоугольника:\n"))
kol_vo=0
x=[0,]
y=[0,]
x.append(a)
y.append(0)
x.append(a)
y.append(b)
x.append(0)
y.append(b)
x.append(0)
y.append(0)
colors  = ["red","green","blue","orange","purple","pink","yellow"]
c = random.choice(colors)
print("Всего квадратов - {}".format(squares(a, b,c)))

plot(x,y,"C0")
show()