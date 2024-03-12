from Modelos.Reserva import Reserva
from Vistas.Vista_Reserva import Vista_Reserva
from datetime import datetime, timedelta
from Controladores.Controlador_Fecha import Controlador_Fecha
from Modelos.Servicios import Servicios
from Controladores.Controlador_Servicios import Controlador_Servicio
from Controladores.Controlador_Persona import Controlador_Persona

class Controlador_Reserva():
    def __init__(self,modelo = Reserva(), vista = Vista_Reserva(),modelofecha = Controlador_Fecha() , modeloservicios = Controlador_Servicio(),modelousuario = Controlador_Persona()):
        self.modelo = modelo
        self.vista = vista
        self.modelofecha = modelofecha
        self.modeloservicios = modeloservicios
        self.modelousuario = modelousuario
        self.reservas = []

    def leer_reservas(self):
        with open("E:\\programas\\T.P.I\\reservas.csv","r") as f:
            for line in f:
                line = line.split(";")
                reserva = Reserva(line[0],line[1],int(line[2]),line[3],line[4],line[5],line[6])
                self.reservas.append(reserva)
    

    def setear_servicios(self):
        self.modeloservicios.leer_productos()
        
    def registrar_reserva(self):
        self.vista.divisor()
        #setear fecha
        try:
            self.modelofecha.leer_fechas()
        
        
            if self.modelofecha.pedir_fecha():
                self.vista.divisor()
            #setear cliente
                if self.modelousuario.consultar_usuario():
            #setear contratados
                    self.vista.divisor()
                    contratados=self.servicios_contratados()
                    self.modelo.set_servicios(contratados)
                    if len(contratados)==0:
                            self.vista.no_contrato()
            #calcular precio
                    else:
                        self.vista.divisor()
                        self.modelo.set_precio(self.calcular_precio())
                        self.vista.mostrar_precio(self.modelo.get_precio())
                        self.vista.mostrar_seña(self.calcular_senia())
                        self.modelo.set_estado("-")
                        self.escribir_archivo()
            else:
                self.vista.divisor()
                self.modelofecha.proxima_fecha()
        except FileNotFoundError:
            self.vista.divisor()
            self.vista.error_leer_archivo()
            

    def cancelar_reserva(self):
        self.vista.divisor()
        try:
            self.leer_reservas()
            f = open("E:\\programas\\T.P.I\\reservas.csv","w")
            b = 1
            validador=True
            while b == 1:
                try:
                    a = self.vista.pedir_dia()
                    b = 2
                except ValueError:
                    self.vista.error_fecha()
                    b = 1
            for reservas in self.reservas:
                if (f'{str(reservas.get_dia()).zfill(2)}/{str(reservas.get_mes()).zfill(2)}/{reservas.get_anio()}') == str(a):
                    self.vista.cancelacion_con_exito()
                    validador=False
                    self.vista.divisor()
                    fechaactual = self.modelofecha.fecha_actual()
                    fechaactual = datetime.strptime(fechaactual, "%d/%m/%Y").date()
                    a = datetime.strptime(a, "%d/%m/%Y").date()
                    if a - fechaactual <= timedelta(days=15):
                        
                        self.vista.no_devolucion()
                    else:
                        
                        precio = float(reservas.get_precio())*(0.06)
                        self.vista.mostrar_devolucion(round(precio,2)) 
                else:
                    f.write(f"{reservas.get_dia()};{reservas.get_mes()};{reservas.get_anio()};{reservas.get_dni()};{reservas.get_servicios()};{reservas.get_precio()};{reservas.get_estado()};\n")
            if validador:
                self.vista.no_fecha()
        except FileNotFoundError:
            self.vista.error_leer_archivo()
        

    def escribir_archivo(self):
        serv=[]
        for i in self.modelo.get_servicios():
            serv.append(i.get_info())
        
        with open("E:\\programas\\T.P.I\\reservas.csv","a") as f:
            f.write(f"{self.modelofecha.obtener_fecha()}{self.modelousuario.obtener_datos()};{serv};{self.modelo.get_precio()};-;\n")
            
    def servicios_contratados(self):
        serv=[]
        contratados=[]
        a=1
        self.vista.servicios_a_contratar()
        for i in self.modeloservicios.get_servicios():
            serv.append(i)
        opciones=len(serv)
        for i in serv:
            self.vista.mostrar(f'{i.get_info()}')
        while (len(serv)>=1):
                validador=False
                a=self.vista.ingrese_serv()
                if a!='fin' and a!='todos':
                    try:
                        for i in serv:
                            if int(a) == i.get_id():
                                contratados.append(i)
                                serv.remove(i)
                                validador=True
                        if int(a)>0 and int(a)<=opciones and validador==False:
                                self.vista.servicio_ya_contratado()
                                validador=True
                        if not validador:
                            self.vista.servicio_inexistente()
                    except ValueError:
                        self.vista.valor_invalido()
                elif a=='fin':
                    serv=[]
                elif a=='todos':
                    contratados=self.modeloservicios.get_servicios()
                    serv=[]
                for i in serv:
                    self.vista.mostrar(f'{i.get_info()}')
        return(contratados)

    def calcular_precio(self):
        precio=0
        for i in self.modeloservicios.get_servicios():
            for k in self.modelo.get_servicios():
                if i.get_id()==k.get_id():
                    precio=precio+i.get_precio()
        precio = (precio+(precio*0.70)) #Gastos administrativos
        precio = (precio + (precio*0.21)) # I.V.A.
        return(precio)
    def calcular_senia(self):
        precio = self.modelo.get_precio()
        precio = (precio*0.30)
        return precio
    def menu_reserva(self):
        a=1
        while a ==1 or a==2:
            self.vista.mostrar_menu_reserva()
            a=self.vista.pedir_dato()
            if a==1:
                self.registrar_reserva()
            elif a==2:
                self.cancelar_reserva()
                
    def ejecutar_menu(self):
        self.setear_servicios()
        a=1
        while a ==1 or a==2 or a==3:
            self.vista.mostrar_menu()
            a=self.vista.pedir_dato()
            if a==1:
                self.menu_reserva()
            elif a==2:
                self.modelousuario.menu_cliente()
            elif a==3:
                self.modeloservicios.menu_servicios()