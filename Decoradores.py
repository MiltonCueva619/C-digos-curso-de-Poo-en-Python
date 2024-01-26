# Decorador es una funcion que decora a otra, le agrega un codigo extra antes o al final

# Creamos la funcion a la cual le envaimos una funcion como parametro 
def decorador(funcion):
    def funcion_modificada():
# Ejecuta un codigo antes
        print("Antes de llamar a la funcion")
# Ejecuta la funcion que le pasamos 
        funcion()
# Ejecuta un codigo despues de la funcion 
        print("Despues de llamar a la funcion")
# Despues devuelve la nueva funcion modificada que primero ejecuta un codigo, luego ejecuta la funcion que se le paso
# y al final ejecuta un codigo despues de la funcion. 
    return funcion_modificada

# Creamos la funcion saludo que imprimira un Hola mundo 
def saludo():
    print("Hola mundo")

# Creamos una variable para guardar ahi la funcion saludo pero decorada
saludo_modificado = decorador(saludo)
# A esa variable le ponremos los parentesis y ya aparecera decorada
saludo_modificado()
 
# Otra manera de utilizar el decordor
@decorador
# Le pasamos la funcion que decorarar
def despedida():
    print("Chao")
# Y nos devolvera la funcion decorada
despedida()
