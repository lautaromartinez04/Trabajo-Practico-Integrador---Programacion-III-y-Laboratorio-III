class Fecha():
    def __init__(self,dia= '',mes = '',anio= ''):
        self._dia = dia
        self._mes = mes
        self._anio = anio
    #Setters
    def set_dia(self,x):
            self._dia = x
    def set_mes(self,x):
        self._mes = x
    def set_anio(self,x):
        self._anio = x
    #Getters
    def get_dia(self):
        return self._dia
    def get_mes(self):
        return self._mes
    def get_anio(self):
        return self._anio
    def get_fecha(self):
        return(f'{self.get_dia()};{self.get_mes()};{self.get_anio()};')
    def get_fecha_visual(self):
        return(f'{self.get_dia()}/{self.get_mes()}/{self.get_anio()}')

    def __str__(self):
        return(f'{self.get_dia()};{self.get_mes()};{self.get_anio()};')

        
                    
