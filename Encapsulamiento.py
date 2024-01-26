#Encapsulamiento    
class MiClase:
    def __init__(self):
#Definimos q es privado por el guion bajo  
        self._atributo_privado = "valor"
#Metodos privados
    def _hablar(self):
        print("Hola estoy hablando")
        
#creamos un objeto        
objeto = MiClase()
#Imprime valor por que entiende que es privado pero si lo pude mostar
print(objeto._atributo_privado)      
print(objeto._hablar())
