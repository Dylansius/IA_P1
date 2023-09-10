class Usuarios:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def muestra_datos(self):
        print("El nombre del usuario es: " + self.nombre, self.edad)
        
usuario1 = Usuarios("Dylan", 22)
print(usuario1.nombre, usuario1.edad)

del usuario1

print(usuario1.nombre, usuario1.edad)