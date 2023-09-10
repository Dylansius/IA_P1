class Usuarios():
    def __init__(self, nombre, pin):
        self.nombre=nombre
        self.pin=pin
    
    def saludo(self):
        print("Saludos " + self.nombre + ". Iniciaste sesion correctamente.")
        
    def despedida(self):
        print(self.nombre + ", cerraste la sesion.")
        
usuario1=Usuarios("Dylan", "21110349")

usuario2=Usuarios("Fabian", "21110346")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()
usuario2.despedida()