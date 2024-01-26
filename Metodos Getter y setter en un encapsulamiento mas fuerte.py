# Metodos Getter y setter en un encapsulamiento mas fuerte

# Creamos una clase con atributos muy privados
class Personaje: 
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
 
# Creamos metodo getter para obtener el nombe        
    def get_nombre(self):
        return self.__nombre
 
# Creamos el metodo setter para modificar el nombre    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

# Creamos el objeto dalto con nombre y edad
dalto = Personaje("Naoh", 11)

# Con el metodo getter obtenemos el nombre y lo imprimimos
nombre = dalto.get_nombre()
print(nombre)

# Creamos una variable para gaurdar ahi el nombre que el usuario nos indique
caracter = input("Ingrese el nombre del Personaje: ")

# COn el metodo setter modificamos el nombre del objeto y le ponemos el que el usuario escribio
dalto.set_nombre(caracter)

# Obtenemos con el metodo getter el nuevo nombre y lo imprimimos
nombre = dalto.get_nombre()
print("El nombre de tu personaje es ", nombre)

        