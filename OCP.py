#OCP, Tienen q estar abiertas para la expansion pero no para modificarlas
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplemented
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")
        
class NoticadorSMS(Notificador):
    def Notificar(self):
            print(f"Enviado por SMS a {self.usuario.sms}")
            
class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviado por Whatsapp a {self.usuario.whatsapp}")
        
class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando twit a {self.usuario.whatsapp}")
        
            
    
    