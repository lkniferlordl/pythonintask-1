﻿#Нурахмедова Камиля Наилевна
#Вариант 10
#Создайте игру, в которой компьютер загадывает название одной из трех стран,
#входящих в военно-политический блок "Тройственный союз", а игрок должен его угадать.
#Задача 6. 
import random
x=random.choice(["Германия", "Австро-Венгрия", "Италия"])
print ("Программа случайным образом загадывает название одной из трёх стран, входящих в Тройственный союз, а игрок должен его угадать")
name=input("Назовите одну из стран, входящую в Тройственный союз:")

if name==x:
	print("Правильно!")
else:
	print ("Вы не угадали!")


input("\n\nНажмите Enter для выхода.")