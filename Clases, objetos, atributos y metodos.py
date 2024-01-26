#Clases, objetos, atributos y metodos
class Celular:
    def __init__(self, marca, modelo, camara):
    #Atributos
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara 
    
    #Metodos    
    def llamar(self):
        print(f"estas llamando desde tu {self.marca} {self.modelo}")
        
    def cortar(self):
        print(f"cortaste la llamada desde tu {self.marca} {self.modelo}")

#cosntructor para objetos 
celular1 = Celular("Iphone ","Iphone 15", "48MP")
celular2 = Celular("Samsung ","S23", "54MP")

celular1.llamar()
celular1.cortar()

celular2.llamar() 
celular2.cortar()



    
      
      


