#Polimorfismo
#creamos clase
class Gato ():
    def sonido (self):
        return "Miau"
    
class Perro ():
    def sonido(self):
        return "guau" 

#1ra manera de hacer Polimorfismo    
gato = Gato()
perro = Perro()
    
print(gato.sonido())
print(perro.sonido())
 
# 2da manera de hacer polimorfismo
def hacer_sonido(animal):
    print(animal.sonido())    
    
hacer_sonido(gato)

print("Como hace el perro ?", perro.sonido)
    