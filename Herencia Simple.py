class Persona: 
     def __init__(self, nombre, edad, nacionalidad):
         self.nombre = nombre
         self.edad= edad
         self.nacionalidad = nacionalidad
         
     def hablar(self):
        print(f"Hola soy {self.nombre} y estoy hablando un poco")
         
class Empleado(Persona): 
    def __init__ (self, nombre, edad, nacionalidad, trabajo, salario): 
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

mario = Empleado("Mario", 45, "ecuatoriano", "Desarrollador", "1500 dolares")
mario.hablar()

class Estudiante(Persona): 
    def __init__(self, nombre, edad, nacionalidad, universidad, carrera):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.carrera = carrera
        
milton = Estudiante("Milton", 24, "Ecuatoriano", "Universidad de las Fuerzas Armadas ESPE", "Ingenieria en Tecnologias de la Informacion")
print("El estudiante", milton.nombre, "tiene", milton.edad, "años de edad, estudia en la", milton.universidad, "la carrera", milton.carrera)
milton.hablar()



    
    
      