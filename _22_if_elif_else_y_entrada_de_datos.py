edad = int(input('Cual es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres un BOOMER.')
elif edad >= 45 and edad <= 100:
	print('Eres mayor de edad.')
elif edad >=100 and edad <= 120:
	print('ERROR nadie puede vivir tanto.')
else:
	print('Edad no valida.')
