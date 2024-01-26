class Animal: 
    def comer(self):
        print("come")
    
    
class Mamifero(Animal):
    def amamantar(self):
        print("amamanta")
        
class Ave(Animal): 
    def volar (self):
        print("vuela")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago2 = Murcielago()

murcielago2.comer()
murcielago2.amamantar()
murcielago2.volar()

    
    
    
    
         