class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"la edad de la persona es: {self.edad}")     
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__( nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"El grado del estudiante es: {self.grado} grado")
        
estudiante = Estudiante("Carlos", 24, "quinto")
estudiante.mostrar_datos()
estudiante.mostrar_grado()
 
    
         
    