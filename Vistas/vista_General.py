class Vista_General: 
    def __init__(self) -> None:
        pass
    

    def pedir_dia(self):
        try:
            return int(input("Digite el dia(dd): "))
        except ValueError:
            return('f')
    
    def pedir_mes(self):
        try:
            return int(input("Digite el mes(mm): "))
        except ValueError:
            return('f')
    
    def pedir_anio(self):
        try:
            return int(input("Digite el anio(aaaa): "))
        except ValueError:
            return('f')
    
    def fecha_registrada(self):
        print ("La fecha esta disponible")
    
    def fecha_invalida(self):
        print("No es posible reservar esa fecha")
    
    def fecha_no_registrada(self):
        print("La fecha esta ocupada")
    
    def valor_invalido(self):#
        print("Valor no valido")
        
    def prox_fecha(self,dato):
        print(f'La proxima fecha disponible es: {dato}\nsi desea utilizar esta fecha, comience de nuevo ingresando esa fecha')
    
    
  
    def pedir_nombre(self):
        return(str(input("Digite el nombre del cliente: ")))
    
    def pedir_apellido(self):
        return str(input("Digite el apellido del cliente: "))
    
    def pedir_dni(self):
        a = 1
        while a == 1:
            try:
                b = int(input("Digite el D.N.I del cliente: "))
                a = 2 
            except ValueError:
                print('valor no valido') 
        return b
    
    def siono(self):
        return(input('El Cliente Existe? y/n '))
    
    def agregado_con_exito(self):
        print('Agregado con exito')
        
    def cliente_existe(self):
        print('Cliente existe')
    
    def mostrar(self,dato):
        print(dato)
        
    def mostrar_menu_cliente(self):
        print('------------CLIENTE------------')
        print('1 - Agregar cliente           ')
        print('2 - Eliminar cliente           ')
        print('Otro - Salir                   ')

            
    def no_dni(self):
        print('No se encontro dni')
    
    def eliminado(self):
        print('Eliminado')
    
    def mostrar_menu(self):
        print('-------------MENU--------------')
        print('1 - Menu Reserva               ')
        print('2 - Menu Clientes              ')
        print("3 - Menu Servicios             ")
        print('Otro - Salir                  ')
        
    def pedir_dato(self):
        try:
            b = int(input())
            a = 2 
            return(b)
        except ValueError:
            return(7)
    


    def pedir_id_serv(self):
        return(input('Ingrese ID del producto: '))
    
    def cambiar_precio(self):
        print('Usted va a cambiar el precio de: ')
    
    def pedir_precio(self):
        a=1
        while a!=int:
            try:
                a=int(input('Ingrese nuevo precio:'))
                return (a)
            except ValueError:
                print('Valor invalido')
            
    def mostrar_menu_servicios(self):
        print('------------SERVICIOS----------')
        print('1 - Agregar servicio           ')
        print('2 - Eliminar servicio          ')
        print("3 - Editar precio servicio     ")
        print('Otro - Salir                   ')
        
            
    def pedir_nombre_servicio(self):
        return(input('Ingrese el nombre del nuevo servicio: '))
    
    def error_leer_archivo(self):
        print("Archivo no encontrado")
        print("Por favor crearlo")
    
    def error_leer_archivo_servicios(self):
        print("Archivo no encontrado")
        
    def divisor(self):
        print('-------------------------------')