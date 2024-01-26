#ISP, ningun cliente debe ser forzado a depender de interfaces que no use 
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass   

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador):    
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")
        
class Robot(Trabajador):    
    def comer(self):
        pass
    
    def trabajar(self):
        print("El robot esta trabajando")
    
    def dormir(self):
        pass
    
robot = Robot()
humano = Humano()
  
humano.comer()   
robot.trabajar()