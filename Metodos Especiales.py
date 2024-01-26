# Metodos especiales, 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad ={self.edad})"
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor= self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
javier = Persona ("Alex",25)
print(javier)

lista = (1,2,3)
print(lista)

repre = repr(javier)
resultado = eval(repre)
print(resultado.edad)
print(resultado.nombre)

ana = Persona("Ana",22)
carlos = Persona("Carlos",26)
nueva_persona = javier + carlos +ana
print(nueva_persona.nombre)
print(nueva_persona.edad)

