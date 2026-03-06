from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarValor, nombre_valido, validarEnteroConRango

ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_HERRAMIENTAS = "herramientas.json"
ARCHIVO_SOLICITUDES = "solicitudes.json"

def reporteStockBajo():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    print('*** REPORTE DE STOCK BAJO ***')
    encontrado = False
    for elemento in herramientas:
        if elemento["cantidad_disponible"] < 3:
            print(f"ID: {elemento['id']} -> {elemento['nombre']} -> Stock: {elemento['cantidad_disponible']}")
            encontrado = True
    if not encontrado:
        print('Todas las herramientas tienen un stock superior a 3.')

def reporteHerramientas():
    prestamos = cargar(ARCHIVO_PRESTAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    
    if not prestamos:
        print('No hay historial de préstamos.')
        return

    print('*** HERRAMIENTAS MÁS SOLICITADAS ***')
    for elemento in herramientas:
        contador_aux = 0
        for p in prestamos:
            if p["herramienta_id"] == elemento["id"]:
                contador_aux += 1
        if contador_aux > 0:
            print(f"Herramienta: {elemento['nombre']} Total préstamos: {contador_aux}")
            