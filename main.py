# 1.Записывается число N от 0 до 99
# 2.Числа через пробел Рацианальные положительные (Запишем в списко или блокнот)
# 3.Найти максимальное число
# Использовал дроби: 28/9 31/9 27/4 28/7 27/5 243994/10204 194787408/12082347 99/14 2938/27 9312/1654
from fractions import Fraction
#2.2 Задание| функция для работы с рацианальными числами
def fract(numA,numB):
    num = Fraction(numA, numB)
    return num


# 1, 2.1 Задание
n = int(input("Введите число < 100: "))
fractions_demo = input()
res_fractions = fractions_demo.replace('/', ' ')
mas = [int(x) for x in res_fractions.split()]
fract_mas = []
if len(mas) == 2*n:
    True
else:
    exit("Примеров больше чем вы задали число n")
for i in range(0,len(mas),2):
    fract_mas.append(fract(mas[i], mas[i+1]))
#3
print("Максимальное число: ", max(fract_mas))

