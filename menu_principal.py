from validaciones import validarMenu
from menu_admin import gestionarUsuario, gestionarHerramientas, gestionarPrestamos, gestionarReportes
from gestionar_usuario import guardar_solicitud
from gestionar_herramientas import listar_herramientas
def menuUsuario():
    print('Bienvenido al programa de consulta de herramientas usuario.')
    while True:
        op=validarMenu('''
                        1. Consultar estado
                        2. Crear Solicitud
                        3. Salir
                        ''',1,3)
        while op==None:
           op=validarMenu('Error, intentelo nuevamente. ',1,3)
        match op:
            case 1:
                listar_herramientas()
            case 2:
                guardar_solicitud('Bienvenido usuario, porfavor digite lo que desea hacer')
            case 3:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible')
        if op==3: 
            break

def menuAdmin():
    print('Seleccione la opción que desea, admin.')
    while True:
        op=validarMenu('''
                        1. Registar usuario
                        2. Registrar herramientas
                        3. Gestionar prestamos
                        4. Gestionar reportes
                        5. Salir
                        ''',1,5)   
        while op==None:
            op=validarMenu('Error, intentelo nuevamente. ',1,5)
        match op:
            case 1:
                gestionarUsuario()
            case 2:
                gestionarHerramientas()
            case 3:
                gestionarPrestamos()
            case 4:
                gestionarReportes()
            case 5:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible. ')
        if op==5: 
            break
