class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Dylan Yair'
usuario001.apellidos = 'Gutierrez Malacara'

usuario001.imprime_datos()
