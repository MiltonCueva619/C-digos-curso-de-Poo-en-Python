# Decorador @Property

class Persona: 
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

# Este decorador lo q hace es crear un metodo getter y a la funcion convertirla en propiedad        
    @property
    def nombre(self):
        return self.__nombre
 
# Este decorador crea un metodo setter    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
      
# DEcorador deleter elimina valores
    @nombre.deleter
    def nombre(self):
        del self.__nombre

muchacho = Persona("Luis", 25)
nombre = muchacho.nombre
print(nombre)

muchacho.nombre = "Oscar"
nombre = muchacho.nombre
print(nombre)

del muchacho.nombre
print("Holaa")