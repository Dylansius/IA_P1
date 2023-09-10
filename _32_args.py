def colores(*args):
	pass
	print('El total de argumentos en la primera fila es de 4: \n', args[0], args[1],args[2],args[3])	
colores('rojo', 'azul', 'verde', 'amarillo')

def colores2(*args):
	pass
	print('El total de argumentos en la segunda fila es de 3: \n', args[0], args[1],args[2])	
colores2('lila', 'negro', 'rojo')
	
def colores3(*args):
	pass
	print('El total de argumentos en la tercera fila es de 1: \n', args[0])	
colores3('rosa')

def colores4(*args):
	pass
	print('El total de argumentos en la cuarta fila es de 2: \n', args[0], args[1])	
colores4('marron', 'naranja')

def coloresfav(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco esta mal.')
coloresfav('marron', 'verde')

def operacion(*args):
	res = args[0] ++ args[1] ++ args[2] ++ args[3]
	print('El numero', args[0], 'mas el numero', args[1], 'mas el numero', args[2], 'mas el numero', args[3], 'da como resultado:', res)
operacion(5, 10, 18, 20)

