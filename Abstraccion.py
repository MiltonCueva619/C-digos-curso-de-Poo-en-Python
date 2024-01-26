#Abstraccion es ocultar la complejidad interna de un sistema
class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto esta encendido")
# El usuario solamente vera cuando el auto ya esta encendio pero el no sabe que antes de encenderse 
# se reviso que este apagado y despues de revisar se encendio el carro, eso es abstraccion        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
# Usamos la funcion pero que el usuario solo sabe q es para conducir no sabe lo que esta detras
mi_auto.conducir()

            