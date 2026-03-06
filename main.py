from menu_principal import menuUsuario, menuAdmin
from validaciones import validarMenu
import time
from log import registrar_log

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

contraseña=input('Ingrese la clave para cargar el menú principal: ')
if contraseña=='flo75689':
    menuMain()
else:
    print(' Acceso denegado, clave incorrecta')