class Servicios:
    def __init__(self,nombre='',id='',precio=0):
        self._nombre=nombre
        self._id=id
        self._precio=precio
    
    #getters
    def get_nombre(self):
        return(self._nombre)
    def get_id(self):
        return(self._id)
    def get_precio(self):
        return int(self._precio)
    #setters
    def set_nombre(self,dato):
        self._nombre=dato
    def set_id(self,dato):
        self._id=dato
    def set_precio(self,dato):
        self._precio=dato
        
    def get_info(self):
        return(f'Servicio: {self._nombre}, ID: {self._id}, Precio: ${self._precio}')