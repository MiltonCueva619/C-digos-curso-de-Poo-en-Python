class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo 
        self.camara = camara 
        
    def llamar(self):
        print(f"estas llamando desde tu {self.marca} {self.modelo}")
        
    def cortar(self):
        print(f"cortaste la llamada desde tu {self.marca} {self.modelo}")
 
celular1 = Celular("Iphone ","Iphone 15", "48MP")
celular2 = Celular("Samsung ","S23", "54MP")

celular1.llamar()
celular1.cortar()

celular2.llamar() 
celular2.cortar()



    
      
      


