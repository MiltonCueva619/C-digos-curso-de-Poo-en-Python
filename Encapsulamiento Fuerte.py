#Encapsulamiento Fuerte
class Clase:
    def _init__(self):
#Le ponemos doble guion bajo y ya es muy privado    
        self.__atributo_privado = "Valor"
 
#tambien podemos crear metodos privados        
    def __hablar(self):
        print("Hola estoy hablando")
     
objeto2 = Clase()
#Ya no imprime por que el atributo es muy privado
print(objeto2.__hablar())