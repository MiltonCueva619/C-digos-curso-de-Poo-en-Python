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


    
    
      