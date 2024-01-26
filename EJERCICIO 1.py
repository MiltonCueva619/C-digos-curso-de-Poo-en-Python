class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado 
        
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando" )
        
nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
grado = input("Grado al que pertenece: ") 

estudiante = Estudiante(nombre, edad, grado)

print(f"""
        Datos del estudiante: \n\n
        Nombre: {estudiante.nombre} \n 
        Edad: {estudiante.edad} \n
        grado: {estudiante.grado} \n 
    
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()





           
    
        
    
