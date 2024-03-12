from Modelos.Servicios import Servicios
from Vistas.vista_General import Vista_General

class Controlador_Servicio:
    def __init__(self,vista=Vista_General(),modelo=Servicios()):
        self._vista=vista
        self._modelo=modelo
        self._servicios=[]
        self.comprobador=True
        
    def get_servicios(self):
        return(self._servicios)
        
    def leer_productos(self):
        if self.comprobador:
            try:
                archivo = open('E:\\programas\\T.P.I\\servicios.csv','r')
                serv=archivo.read()
                archivo.close()
                serv=serv.split('\n')
                for i in range (len(serv)):
                    serv[i]=serv[i].split(';')
                serv.pop()
                for i in serv:
                    self._servicios.append(Servicios(i[0],int(i[1]),int(i[2])))
                self.comprobador=False
            except FileNotFoundError:
                self._vista.error_leer_archivo_servicios()
        else:
            pass

    def calcular_precio(self,serv):
        precio=0
        for i in self._servicios:
            for k in serv:
                if i.get_nombre()==k:
                    precio=precio+i.get_precio()
        return(precio)
    
    def actualizar_precio(self):
        self._vista.divisor()
        try:
            self.leer_productos()
            a=1
        except FileNotFoundError:
            self._vista.error_leer_archivo_servicios()
        if a == 1:
            archivo=open('E:\\programas\\T.P.I\\servicios.csv','w')
            for i in self._servicios:
                self._vista.mostrar(i.get_info())
            self._vista.divisor()
            a=self._vista.pedir_id_serv()
            for i in self._servicios:
                if int(a)==i.get_id():
                    self._vista.divisor()
                    self._vista.cambiar_precio()
                    self._vista.mostrar(i.get_info())
                    i.set_precio(self._vista.pedir_precio())
                    self._vista.divisor()
                    self._vista.mostrar(i.get_info())
                archivo.write(f'{i.get_nombre()};{i.get_id()};{i.get_precio()}\n')
            archivo.close()
        
    def eliminar_servicio(self):
        self._vista.divisor()
        validador=True
        try:
            self.leer_productos()
            a=1
        except FileNotFoundError:
            self._vista.error_leer_archivo_servicios()
        if a == 1:
            cant=len(self._servicios)
            archivo=open('E:\\programas\\T.P.I\\servicios.csv','w')
            for i in self._servicios:
                self._vista.mostrar(i.get_info())
            self._vista.divisor()
            a=self._vista.pedir_id_serv()
            try:
                if int(a)<=cant and int(a)>0:
                    for i in self._servicios:
                            if int(a)==i.get_id():
                                self._vista.divisor()
                                self._vista.mostrar(i.get_info())
                                self._servicios.remove(i)
                                self._vista.eliminado()
                else:
                    self._vista.divisor()
                    self._vista.valor_invalido()
            except ValueError:
                            validador=False
            if not validador:
                self._vista.divisor()
                self._vista.valor_invalido()
            for i in self._servicios:
                archivo.write(f'{i.get_nombre()};{i.get_id()};{i.get_precio()}\n')
            archivo.close()
            
                
    def menu_servicios(self):
        a=1
        while a ==1 or a==2 or a==3:
            self._vista.mostrar_menu_servicios()
            a=self._vista.pedir_dato()
            if a==1:
                pass
                self.agregar_servicio()
            elif a==2:
                self.eliminar_servicio()
            elif a==3:
                self.actualizar_precio()
                
    def agregar_servicio(self):
        self._vista.divisor()
        try:
            self.leer_productos()
            a=1
        except FileNotFoundError:
            self._vista.error_leer_archivo_servicios()
        if a == 1:
                comprobador=True
                archivo=open('E:\\programas\\T.P.I\\servicios.csv','a')
                nombre=self._vista.pedir_nombre_servicio()
                ide=1
                for i in self._servicios:
                    if ide == i.get_id():
                        comprobador=False
                    if not comprobador:
                        ide+=1
                        comprobador=True
                precio=self._vista.pedir_precio()
                self._servicios.append(Servicios(nombre,ide,precio))
                archivo.write(f'{nombre};{ide};{precio}\n')
                self._vista.divisor()
                self._vista.mostrar(self._servicios[(len(self._servicios))-1].get_info())
                self._vista.divisor()
                archivo.close()