class Userypass:
    def __init__(self, nombre="",paterno="", materno="", usuario="", Pass="",direccion="", telefono=0,iduser=0):
        self.nombre=nombre
        self.paterno=paterno
        self.materno=materno
        self.usuario=usuario
        self.Pass=Pass
        self.direccion=direccion
        self.telefono=telefono
        self.iduser=iduser
        
    def Nuevo():
        print("Usuario nuevo")
        
    def Bajas():
        print("El usuario ha sido dado de baja")
        
    def Validar():
        print("Es correcto")
        
    def CambiarPass():
        print("La contraseña se modifico")