def vozrast (age) :
	try :
		age_int = int(age)
		if age_int >0:
			if age_int <= 7 :
				print("В детский сад")
				return
			if age_int <= 16 :
				print("В школу")
				return
			if age_int <= 23 :
				print("В университет")
				return
			if age_int <= 65 :
				print("На работу")
				return
		else:
			print("Введено отрицательное число")
	except ValueError :
		print("Введено не число")
vozrast (input('Введите ваш возраст: ')) #пользователь вводит возраст