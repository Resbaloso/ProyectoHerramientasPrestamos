from validaciones import validarMenu
from gestionar_usuario import guardar_solicitud, listar_solicitudes, eliminar_solicitud
from gestionar_herramientas import guardar_herramienta, listar_herramientas, eliminar_herramienta, buscar_herramienta, actualizar_estado_herramienta,actualizar_stock_herramienta
from gestionar_prestamos import guardar_prestamo, listar_prestamos, devolver_herramienta
from gestionar_reportes import reporteHerramientas, reporteStockBajo

def gestionarUsuario():
    print('Ha ingresado al menú de gestionar usuario.')
    while True:
        op=validarMenu('''
                        1. Guardar Solicitud Nueva
                        2. Listar Solicitudes
                        3. Eliminar Solicitudes
                        4. Salir
                        ''',1,4)
        while op==None:
           op=validarMenu('Error, intentelo nuevamente. ',1,4)
        match op:
            case 1:
                guardar_solicitud('Bienvenido admin, ingrese la solicitud')
            case 2:
                listar_solicitudes()
            case 3:
                eliminar_solicitud()
            case 4:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible')
        if op==4: 
            break

def gestionarHerramientas():
    print('Ha ingresado al menú de gestionar herramientas.')
    while True:
        op=validarMenu('''
                        1. Guardar Herramienta Nueva
                        2. Listar Herramientas
                        3. Eliminar Herramienta
                        4. Buscar Herramienta
                        5. Actualizar Estado Herramienta
                        6. Actualizar Stock Herramienta
                        7. Salir
                        ''',1,7)
        while op==None:
           op=validarMenu('Error, intentelo nuevamente. ',1,7)
        match op:
            case 1:
                guardar_herramienta()
            case 2:
                listar_herramientas()
            case 3:
                eliminar_herramienta()
            case 4:
                buscar_herramienta()
            case 5:
                actualizar_estado_herramienta()
            case 6:
                actualizar_stock_herramienta()
            case 7:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible')
        if op==7: 
            break

def gestionarPrestamos():
    print('Ha ingresado al menú de gestionar prestamos.')
    while True:
        op=validarMenu('''
                        1. Guardar Prestamo
                        2. Listar Prestamos
                        3. Devolver Herramienta
                        4. Salir
                        ''',1,4)
        while op==None:
           op=validarMenu('Error, intentelo nuevamente. ',1,4)
        match op:
            case 1:
                guardar_prestamo()
            case 2:
                listar_prestamos()
            case 3:
                devolver_herramienta()
            case 4:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible')
        if op==4: 
            break

def gestionarReportes():
    print('Ha ingresado al menú de gestionar reportes.')
    while True:
        op=validarMenu('''
                        1. Reporte de stock bajo
                        2. Reporte herramientas más solicitadas
                        3. Salir
                        ''',1,3)
        while op==None:
           op=validarMenu('Error, intentelo nuevamente. ',1,3)
        match op:
            case 1:
                reporteStockBajo()
            case 2:
                reporteHerramientas()
            case 3:
                print('Gracias por usar nuestro servicio. ')
            case _:
                print('No se encuentra la opción, porfavor digite una opción disponible')
        if op==3: 
            break