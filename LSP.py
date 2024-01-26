#LSP, las clases derivadas tienen que ser sustituibles por sus clases base
# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "no puedo volar"
    
# def hacer_volar(ave = Ave):
#     return ave.volar

# print(hacer_volar(Pinguino()))

class Ave:
    pass

class AveVoladora(Ave):
    def volar(delf):
        return "Estoy Volando"
    
class AveNoVoladora(Ave):
    pass
    