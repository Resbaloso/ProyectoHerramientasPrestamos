from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero
from gestionar_herramientas import listar_herramientas, actualizar_estado_herramienta
from gestionar_usuario import listar_solicitudes
from datetime import date, datetime, timedelta
from log import registrar_log

ARCHIVO_SOLICITUDES = "solicitudes.json"
ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_HERRAMIENTAS = "herramientas.json"

def guardar_prestamo():
    prestamos = cargar(ARCHIVO_PRESTAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    
    listar_solicitudes()
    id_usuario = validarEntero("Ingrese el ID del usuario: ")
    
    listar_herramientas()
    id_elemento = validarEntero("Ingrese el ID de la herramienta a prestar: ")
    
    herramienta_encontrada = None
    for elemento in herramientas:
        if elemento["id"] == id_elemento:
            herramienta_encontrada = elemento
            break
            
    if herramienta_encontrada == None:
        msg_error = f"ERROR: Herramienta ID {id_elemento} no encontrada."
        print(msg_error)
        registrar_log(msg_error)
        return

    cantidad = validarEntero(f"¿Cuántas unidades se van a prestar? Disponible: {herramienta_encontrada['cantidad_disponible']}")
    while cantidad == None or cantidad <= 0:
        cantidad = validarEntero("Error, ingrese una cantidad válida mayor a 0")

    if cantidad > herramienta_encontrada["cantidad_disponible"]:
        solicitudes = cargar(ARCHIVO_SOLICITUDES)
        for elemento in solicitudes:
                msg_error = f"ERROR: Stock insuficiente. Usuario con id: {id_usuario}| Nombres: {elemento["nombres"]}| Apellidos: {elemento["apellidos"]} pidio {cantidad} de ID {id_elemento}"
                print(msg_error)
                registrar_log(msg_error)
        return

    try:
        dias_prestamo = int(input('Ingrese la cantidad de días que se prestará la herramienta: '))
        fecha_inicio = date.today()
        
        fecha_final_prestamo = fecha_inicio + timedelta(days=dias_prestamo)
    except ValueError:
        registrar_log("ERROR: Se ingresaron dias no numericos en el prestamo")
        print("Error en el formato de días.")
        return

    herramienta_encontrada["cantidad_disponible"] -= cantidad
    guardar(ARCHIVO_HERRAMIENTAS, herramientas)

    obs = input("Observaciones: ")

    nuevo_prestamo = {
        "id": generar_id(prestamos),
        "usuario_id": id_usuario,
        "herramienta_id": id_elemento,
        "cantidad": cantidad,
        "fecha_inicio": str(fecha_inicio),
        "fecha_estimada": str(fecha_final_prestamo),
        "estado": "Activo",
        "observaciones": obs
    }
    
    prestamos.append(nuevo_prestamo)
    guardar(ARCHIVO_PRESTAMOS, prestamos)
    
    registrar_log(f"EXITO: Prestamo ID {nuevo_prestamo['id']} creado. Devolucion: {fecha_final_prestamo}")
    print(f'¡PRESTAMO REGISTRADO! Debe devolverse el: {fecha_final_prestamo}')

def devolver_herramienta():
    contador_aux = 0
    prestamos = cargar(ARCHIVO_PRESTAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    
    print("*** DEVOLUCION DE HERRAMIENTAS ***")
    id_p = validarEntero("Ingrese el ID del prestamo a finalizar")
    
    for p in prestamos:
        if p["id"] == id_p and p["estado"] == "Activo":

            for h in herramientas:
                if h["id"] == p["herramienta_id"]:
                    h["cantidad_disponible"] += p["cantidad"]
                    break
            
            p["estado"] = "Devuelto"
            
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            guardar(ARCHIVO_PRESTAMOS, prestamos)
            print(f"¡Herramienta devuelta! Se restauraron {p['cantidad']} unidades al stock.")
            return
        contador_aux += 1
        
    msg_error = f"ERROR: El prestamo ya habia sido cancelado o la herramienta ya habia sido prestada. "
    print(msg_error)
    registrar_log(msg_error)

def listar_prestamos():
    prestamos = cargar(ARCHIVO_PRESTAMOS)
    if not prestamos:
        print("No hay prestamos registrados.\n")
        return

    print("*** LISTADO DE PRESTAMOS ***")
    for p in prestamos:
        print(f"ID: {p['id']} | Usuario: {p['usuario_id']} | Herramienta ID: {p['herramienta_id']} | Cant: {p['cantidad']} | Estado: {p['estado']}")
    print()