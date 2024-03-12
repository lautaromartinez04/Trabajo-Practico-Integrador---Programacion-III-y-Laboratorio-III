from Vistas.vista_General import Vista_General

class Vista_Reserva(Vista_General):
    def __init__(self) -> None:
        pass

    def cancelacion_con_exito(self):
        print("Se cancelo la reserva con exito")

    def error_dni(self):
        print("Digito un D.N.I no valido")
    
    def servicio_inexistente(self):
        print("el servicio no existe:")
    
    def no_fecha(self):
        print("No se encontro fecha")
        
    def servicios_a_contratar(self):
        print("los servicios que puede contratar son ('fin' para finalizar, 'todos' para seleccionar todos los servicios): ")
        
    def ingrese_serv(self):
        try:
            return input(('ingrese ID del servicio: '))
        except ValueError:
            print('valor invalido')
    
    def servicio_ya_contratado(self):
        print("ya contrato ese servicio")
        
    def no_contrato(self):
        print("no contrato ningun servicio")
        
        
    def mostrar_menu_reserva(self):
        print('------------EVENTOS------------')
        print('1 - registrar evento           ')
        print("2 - cancelar evento            ")
        print('otro - salir                   ')

    
    def pedir_dia(self):
        try:
            return(input('ingrese fecha del evento(dd/mm/aaaa): '))
        except ValueError:
            print('valor invalido')
            
    def error_fecha(self):
        print('fecha no registrada')
        
    def no_devolucion(self):
        print('no le corresponde devolucion de la seña.')
    
    def mostrar_precio(self,x):
        print(f"El monto total del evento es ${x}")

    def mostrar_seña(self,x):
        print(f"El monto minimo a señar es ${x}")

    def mostrar_devolucion(self,x):
        print(f"Se le debe devolver al cliente ${x}")