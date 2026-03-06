from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarMenu, nombre_valido
from gestionar_herramientas import listar_herramientas

ARCHIVO = "solicitudes.json"

def guardar_solicitud(mensaje):
    solicitudes = cargar(ARCHIVO)
    print(mensaje)

    nombres = input('Ingrese los nombres: ')
    while nombre_valido(nombres) == False:
        nombres = input('Error. Ingrese nombres válidos: ')

    apellidos = input('Ingrese los apellidos: ')
    while nombre_valido(apellidos) == False:
        apellidos = input('Error. Ingrese apellidos válidos: ')

    telefono = input('Ingrese el teléfono: ')
    while nombre_valido(telefono) == False:
        telefono = input('Error. Ingrese un teléfono válido: ')

    direccion = input('Ingrese la dirección: ')
    while nombre_valido(direccion) == False:
        direccion = input('Error. Ingrese una dirección válida: ')
    
    print('Mire la lista de aquí abajo y escriba que desea utilizar')
    listar_herramientas()
    print('Estados: 1. Activa, 2. En reparacion, 3. Fuera de servicio ')
    herramienta = input('Ingrese la herramienta solicitada: ')
    while nombre_valido(herramienta) == False:
        herramienta = input('Error. Ingrese una herramienta válida: ')

    nueva_solicitud = {
        "id": generar_id(solicitudes),
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "herramienta": herramienta
    }  
    solicitudes.append(nueva_solicitud)
    guardar(ARCHIVO, solicitudes)
    print(f'¡SOLICITUD REGISTRADA CON ÉXITO!')

def listar_solicitudes():
    solicitudes = cargar(ARCHIVO)
    
    if not solicitudes:
        print("No hay solicitudes registradas.")
        return

    print('\n*** LISTADO DE SOLICITUDES ****')
    for elemento in solicitudes:
        print(f"ID: {elemento['id']} Cliente: {elemento['nombres']} {elemento['apellidos']} Telefono: {elemento['telefono']} Herramienta: {elemento['herramienta']}")
    print()

def eliminar_solicitud():
    solicitudes = cargar(ARCHIVO)
    if not solicitudes:
        print("No hay solicitudes para eliminar.")
        return
    listar_solicitudes()
    id_buscado = validarEntero("Ingrese el ID de solicitud a eliminar")
    while id_buscado is None:
        id_buscado = validarEntero("Error, ingrese un ID válido") 
    for elemento in range(len(solicitudes)):
        if solicitudes[elemento]["id"] == id_buscado:
            solicitudes.pop(elemento)
            guardar(ARCHIVO, solicitudes)
            print('¡Solicitud eliminada!')
            return
            
    print("El ID de solicitud no existe. ")

