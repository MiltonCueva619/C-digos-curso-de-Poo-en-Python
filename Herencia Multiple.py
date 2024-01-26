class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"{self.nombre} esta hablando")
       
class Artista: 
    def __init__(self, habilidad): 
        self.habilidad = habilidad 
        
    def mostrar_habilidad(self):
        return f"{self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
        
    def presentarse(self):
        print(f"Hola soy: {self.nombre},tengo la habilidad de {self.mostrar_habilidad()} y trabajo en la empresa {self.empresa} y mi sueldo es {self.salario}")

paul = EmpleadoArtista("Paul", 35, "Ecuatoriano", "Estudiar", "4500", "Nutrigan")

herencia = issubclass(Artista,Persona)
instancia = isinstance(paul, Persona)
print(instancia)




        