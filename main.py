from menu_principal import menuUsuario, menuAdmin
from validaciones import validarMenu
import time
from log import registrar_log
from gestionarJson import cargar, guardar
print("Iniciando sistema...")
time.sleep(1)
print("[##        ] 20%")
time.sleep(1)
print("[######    ] 60%")
time.sleep(1)
print("[##########] 100%")
time.sleep(0.5)
print("¡Carga completa!")

def menuMain():
    while True:
        op=validarMenu('''Bienvenido, admim.
                        Porfavor ingrese lo que desea hacer: 
                        1.  Ingresar al menú de comprar de usuarios.
                        2.  Ingresar al menú de Admin.
                        3.  Salir.
                       '''
                        ,1,3)   
        while op==None:
            op=validarMenu('Error, intente nuevamente!',1,3)
        match op:
            case 1:
                menuUsuario()
            case 2:
                menuAdmin()
            case 3:
                print('Gracias por usar nuestro servicio')
            case _:
                print('No se encuentra la opción.')
        if op==3: 
            break


clave_sistema = int(input("Ingrese la clave del sistema requerida: "))


clave_pedida = int(input("Ingrese la clave para cargar el menú principal: "))

if clave_pedida == clave_sistema:
    print("Acceso concedido")
    menuMain()
else:
    print("Acceso denegado, clave incorrecta. Intente nuevamente")