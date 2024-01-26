#Metodos Getter y Setter

#Creamos una clase con dos atributos muy privados, nombre y edad.
class Persona: 
    def __init__(self, nombre,edad):
        self._nombre = nombre
        self._edad = edad

# Creamos el metodo getter para acceder al nombre 
    def get_nombre(self):
        return self._nombre

# Creamos el metodo setter para establecer un nuevo nombre    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

#creamos un objeto llamado joven         
joven = Persona("Javier",25) 

# Llamamos a la funcion para acceder al nombre y luego se imprime
nombre = joven.get_nombre
print(joven._nombre) 

# Utilizamos el metodo setter para cambiar el nombre 
joven.set_nombre("Chinchulin")
print(joven._nombre)

# Con esta opcion podemos cambiarle el nombre por el que queramos
name =input("Ingrese el nombre de su personaje")
joven.set_nombre(name)
print(joven._nombre)

