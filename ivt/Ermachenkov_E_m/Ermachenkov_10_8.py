#Задача 10. Вариант 8.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
#Ermachenkov E. M.
#14.04.2017

points = 30
power = 0
agility = 0
health = 0
wisdom = 0
print('Вас приветствует меню генератора персонажей\nУ вас есть 30 очков\nВыберите номер действия, которое вы бы хотели провести над характеристиками\n1. Повысить характерстики\n2. Уменьшить характеристики\n3. Информация о персонаже\n4. Нажмите для закрытия генератора')
selection = '0'
while selection == '1' or '2' or '3' or '0':
	selection = input()
	if selection == '1':
		print('Выберите характеристику, которую хотите повысить\n1. Сила\n2. Ловкость\n3. Здоровье\n4. Мудрость\n')
		menu = int(input())
		if menu == 1:
			print('Вы выбрали Силу\nвведите число очков, которое хотели бы потратить на эту характеристику')
			numb = int(input())
			if numb <= points:
				power += numb
				points -= numb
				selection = '0'
			elif numb > points:
				print('У вас недостаточно очков, осталось - ', points)
		elif menu == 2:
			print('Вы выбрали Ловкость\nвведите число очков, которое хотели бы потратить на эту характеристику')
			numb = int(input())
			if numb <= points:
				agility += numb
				points -= numb
			elif numb > points:
				print('У вас недостаточно очков, осталось - ', points)
		elif menu == 3:
			print('Вы выбрали Здоровье\nвведите число очков, которое хотели бы потратить на эту характеристику')
			numb = int(input())
			if numb <= points:
				health += numb
				points -= numb
			elif numb > points:
				print('У вас недостаточно очков, осталось - ', points)
		elif menu == 4:
			print('Вы выбрали Мудрость\nвведите число очков, которое хотели бы потратить на эту характеристику')
			numb = int(input())
			if numb <= points:
				wisdom += numb
				points -= numb
			elif numb > points:
				print('У вас недостаточно очков, осталось - ', points)
	elif selection == '2':
		print('Выберите характеристику, которую хотите уменьшить\n1. Сила\n2. Ловкость\n3. Здоровье\n4. Мудрость\n')
		menu2 = int(input())
		if menu2 == 1:
			print('Вы выбрали Силу\nвведите число очков, которое хотели бы отнять от этой характеристики')
			numb = int(input())
			if numb <= power:
				power -= numb
				points += numb
			elif numb > power:
				print('Вы не можете снять столько очков с характеристики, очков силы - ', power)
		elif menu2 == 2:
			print('Вы выбрали Ловкость\nвведите число очков, которое хотели бы отнять от этой характеристики')
			numb = int(input())
			if numb <= agility:
				agility -= nubm
				points += numb
			elif numb > agility:
				print('Вы не можете снять столько очков с характеристики, очков ловкости - ', agility)
		elif menu2 == 3:
			print('Вы выбрали Здоровье\nвведите число очков, которое хотели бы отнять от этой характеристики')
			numb = int(input())
			if numb <= health:
				health -= numb
				points += numb
			elif numb > health:
				print('Вы не можете снять столько очков с характеристики, очков здоровья - ', health)
		elif menu2 == 4:
			print('Вы выбрали Мудрость\nвведите число очков, которое хотели бы отнять от этой характеристики')
			numb = int(input())
			if numb <= wisdom:
				wisdom -= numb
				points += numb
			elif numb > wisdom:
				print('Вы не можете снять столько очков с характеристики, очков мудрости - ', wisdom)
	elif selection == '3':
		print('Характеристики вашего персонажа\nСила - ', power, '\nЛовкость - ', agility, '\nЗдоровье - ', health, '\nМудрость - ', wisdom, '\nУ вас осталось ', points)
	elif selection != '1' or '2' or '3':
		print('Желаете закрыть генератор персонажа? (да/нет)')
		exit = input()
		if exit == 'нет':
			selection = '0'
		elif exit == 'да':
			break 

		
