#Polimorfismo de sobrecarga 

#En python el polimorfismo funciona sin importar el tipo de dato 
num1 = 3
num2 = 4.25

resultado = num1 + num2 

print(resultado)
print(type(num1))

#Polimorfismo en arreglos teniendo q ordenar diferentes tipos de datos

def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
lista1 = [1,2,3,4]
lista2 = "maquina"

recorrer(lista1)
recorrer(lista2)