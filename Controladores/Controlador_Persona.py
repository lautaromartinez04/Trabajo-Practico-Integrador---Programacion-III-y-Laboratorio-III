from Modelos.Persona import Persona
from Vistas.vista_General import Vista_General

class Controlador_Persona:
    def __init__(self,modelo = Persona(),vista = Vista_General()):
        self.modelo = modelo
        self.vista = vista
        self.usuarios=[]
        self.comprobador=True

    def obtener_datos(self):
        return(self.modelo.get_dni())
    
    def leer_usuarios(self):
            if self.comprobador:
                archivo=open("E:\\programas\\T.P.I\\usuarios.csv","r")
                texto=archivo.read()
                archivo.close()
                texto=texto.split('\n')
                texto.pop()
                for i in range(len(texto)):
                    texto[i]=texto[i].split(';')
                    cliente = Persona((texto[i][0]),(texto[i][1]),int(texto[i][2]))
                    self.usuarios.append(cliente)
                self.comprobador=False
        
    def registrar_usuario(self):
        self.vista.divisor()
        comprobador=True
        try:
            self.leer_usuarios()
            self.modelo.set_nombre(self.vista.pedir_nombre())
            self.modelo.set_apellido(self.vista.pedir_apellido())
            self.modelo.set_dni(self.vista.pedir_dni())
            f = open("E:\\programas\\T.P.I\\usuarios.csv","w")
            for i in self.usuarios:
                if int(self.modelo.get_dni())==int(i.get_dni()):
                    comprobador=False
            if comprobador:
                self.vista.agregado_con_exito()
                self.usuarios.append(Persona((self.modelo.get_nombre()),(self.modelo.get_apellido()),(self.modelo.get_dni())))
            else:
                self.vista.cliente_existe()
            
            for i in self.usuarios:
                f.write(f'{i.get_nombre()};{i.get_apellido()};{i.get_dni()}\n')
            f.close()
            return(True)
        except FileNotFoundError:
            self.vista.error_leer_archivo()
        


    def eliminar_usuario(self):
        self.vista.divisor()
        try:
            self.leer_usuarios()
            comprobador=False
            archivo=open("E:\\programas\\T.P.I\\usuarios.csv","w")
            for i in self.usuarios:
                self.vista.mostrar(i.get_info())
            self.vista.divisor()
            a=self.vista.pedir_dni()
            for i in self.usuarios:
                if a==i.get_dni(): 
                    self.vista.mostrar(i.get_info())
                    self.usuarios.remove(i)
                    comprobador = True
            if comprobador == True :
                    self.vista.eliminado()
            elif comprobador == False:
                self.vista.no_dni()
            for i in self.usuarios:
                archivo.write(f'{i.get_nombre()};{i.get_apellido()};{i.get_dni()}\n')
            archivo.close()
        except FileNotFoundError:
            self.vista.error_leer_archivo()
                
                
                
    
    def buscar_usuario(self):
        for i in self.usuarios:
            self.vista.mostrar(f'{i.get_nombre()} {i.get_apellido()} {i.get_dni()}')
        a=self.vista.pedir_dni()
        for i in self.usuarios:
            if a == i.get_dni():
                self.modelo.set_nombre(i.get_nombre())
                self.modelo.set_apellido(i.get_apellido())
                self.modelo.set_dni(i.get_dni())
                return(True)
        return(False)
            
            
    def consultar_usuario(self):
        try:
            self.leer_usuarios()
            a=self.vista.siono()
            if a=='y':
                return(self.buscar_usuario())
            elif a == 'n':
                return(self.registrar_usuario())
        except FileNotFoundError:
            self.vista.error_leer_archivo()
            
        
    def menu_cliente(self):
        a=1
        while a ==1 or a==2:
            self.vista.mostrar_menu_cliente()
            a=self.vista.pedir_dato()
            if a==1:
                self.registrar_usuario()
            elif a==2:
                self.eliminar_usuario()