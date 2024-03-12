from Modelos.Fecha import Fecha
from Vistas.vista_General import Vista_General
from Modelos.Reserva import Reserva
from datetime import datetime, timedelta


class Controlador_Fecha():
    def __init__(self,modelo = Fecha(), vista = Vista_General(),modeloreserva = Reserva()):
        self.modelo = modelo
        self.vista = vista
        self.modeloreserva = modeloreserva
        self.fechas = []
        self.ahora=datetime.now().date()

    def leer_fechas(self):
        f = open("E:\\programas\\T.P.I\\reservas.csv","r")
        for line in f:
            line = line.split(";")
            fecha = Fecha(int(line[0]),int(line[1]),int(line[2]))
            self.fechas.append(fecha)
        f.close()
    
    def comprobar_fecha(self):
        #if self.pedir_fecha():
        fecha_cumplida = False
        for fecha in self.fechas:
            if fecha.get_dia() == self.modelo.get_dia() and fecha.get_mes() == self.modelo.get_mes() and fecha.get_anio() == self.modelo.get_anio():
                fecha_cumplida = True
                break
        if not fecha_cumplida:
            
            return(True)
        return (False)

    def pedir_fecha(self):
        a=1
        while a==1:
            dia=self.vista.pedir_dia()
            mes=self.vista.pedir_mes()
            anio=self.vista.pedir_anio()
            fecha=(f'{dia}/{mes}/{anio}')
            print(fecha)
            try:
                datetime.strptime(fecha, '%d/%m/%Y')
                a=2
                self.modelo.set_dia(dia)
                self.modelo.set_mes(mes)
                self.modelo.set_anio(anio)
            except ValueError:
                self.vista.fecha_invalida()
        if self.comprobar_fecha():
            return self.comprobar_fecha_actual()
                
            
            
            
            
            
            
    def comprobar_fecha_actual(self):
        fecha=(f'{str(self.modelo.get_dia()).zfill(2)}/{str(self.modelo.get_mes()).zfill(2)}/{self.modelo.get_anio()}')
        fecha=datetime.strptime(fecha,'%d/%m/%Y').date()
        if fecha<=self.ahora:
            return False
        return True
        
    def fecha_actual(self):
        fecha=(f'{str(self.ahora.day).zfill(2)}/{str(self.ahora.month).zfill(2)}/{str(self.ahora.year).zfill(4)}')
        return fecha
        
        
    def proxima_fecha(self):
        if not self.comprobar_fecha_actual():
            self.modelo.set_dia(self.ahora.day)
            self.modelo.set_mes(self.ahora.month)
            self.modelo.set_anio(self.ahora.year)
            self.vista.fecha_invalida()
        else:
            self.vista.fecha_no_registrada()
        while not (self.comprobar_fecha()):
            fecha=(f'{str(self.modelo.get_dia()).zfill(2)}/{str(self.modelo.get_mes()).zfill(2)}/{self.modelo.get_anio()}')
            fecha=datetime.strptime(fecha,'%d/%m/%Y').date()
            
            fecha+=timedelta(days=1)
            self.modelo.set_dia(fecha.day)
            self.modelo.set_mes(fecha.month)
            self.modelo.set_anio(fecha.year)
        self.vista.prox_fecha(self.modelo.get_fecha_visual())
            
        
        
        
    def obtener_fecha(self):
        return (self.modelo.get_fecha())