class A:
    def hablar(self):
        print("Hola desde A")
        
class H(A):
    def hablar(self):
        print("Hola desde H")


class B(A): 
    pass
        
class C(H):
    pass
        
class D(B,C): 
        pass

#Creamos un objeto "d" de la clase "D"        
d = D()
d.hablar()

#Ver el orden de ejecucion
print(D.mro())

#Llamar al metodo de H utilizando la clase que hereda a todos
H.hablar(d)