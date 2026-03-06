from gestionarJson import cargar, guardar, generar_id
from validaciones import validarEntero, validarValor, nombre_valido, validarEnteroConRango

ARCHIVO_HERRAMIENTAS = "herramientas.json"

def guardar_herramienta():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    nombre = input('Ingrese el nombre de la herramienta: ')
    while nombre_valido(nombre) == False:
        nombre = input('Error, ingrese un nombre valido: ')

    categoria = input('Ingrese la categoria: ')
    while nombre_valido(categoria) == False:
        categoria = input('Error, ingrese una categoria valida: ')

    cantidad = validarEntero('Ingrese la cantidad disponible: ')
    while cantidad == None or cantidad < 0:
        cantidad = validarEntero('Error, ingrese una cantidad valida: ')

    estado = validarEnteroConRango('Estados: 1. Activa, 2. En reparacion, 3. Fuera de servicio ',1,3)

    valor_estimado = validarValor('Ingrese el valor estimado del arriendo de la herramienta')

    nueva_herramienta = {
        "id": generar_id(herramientas),
        "nombre": nombre,
        "categoria": categoria,
        "cantidad_disponible": cantidad,
        "estado": estado,
        "valor_estimado": valor_estimado
    }

    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO_HERRAMIENTAS, herramientas)
    print('¡HERRAMIENTA GUARDADA CON ÉXITO!')

def actualizar_estado_herramienta():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    listar_herramientas()
    
    id_herramienta = validarEntero("Escoja el id de la herramienta a actualizar ")
    while id_herramienta == None:
        id_herramienta = validarEntero("Error, Escoja el id a actualizar ")

    for elemento in herramientas:
        if id_herramienta == elemento["id"]:
            estado = validarEnteroConRango('Estados: 1. Activa, 2. En reparacion, 3. Fuera de servicio ',1,3)
            elemento["estado"] = estado
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            print('¡Herramienta actualizada con éxito!')
            return
    
    print("La herramienta no existe.")

def listar_herramientas():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    if not herramientas:
        print("No hay herramientas registradas")
        return

    print('*** LISTADO DE HERRAMIENTAS ****')
    for elemento in herramientas:
        print(f"ID: {elemento['id']} -> {elemento['nombre']} -> {elemento['categoria']} -> Stock: {elemento['cantidad_disponible']} -> Estado: {elemento['estado']}")
    print()

def eliminar_herramienta():
    contador_aux = 0
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    
    if not herramientas:
        print("No hay herramientas para eliminar.")
        return

    listar_herramientas()
    id_herramienta = validarEntero("Escoja el id de la herramienta a eliminar")
    
    while id_herramienta == None:
        id_herramienta = validarEntero("Error, escoja un id valido")
        
    for elemento in herramientas:
        if id_herramienta == elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            print('¡Herramienta eliminada!')
            return
        contador_aux += 1
    
    print("La herramienta no existe. ")

def actualizar_stock_herramienta():
    contador_aux = 0
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    
    if not herramientas:
        print("No hay herramientas para modificar stock.")
        return

    listar_herramientas()
    id_herramienta = validarEntero("Escoja el id de la herramienta para modificar su stock")
    
    while id_herramienta == None:
        id_herramienta = validarEntero("Error, escoja un id valido")
        
    for elemento in herramientas:
        if id_herramienta == elemento["id"]:
            print(f"Stock actual de {elemento['nombre']}: {elemento['cantidad_disponible']}")
            
            nueva_cantidad = validarEntero("Ingrese la nueva cantidad de stock disponible")
            while nueva_cantidad == None or nueva_cantidad < 0:
                nueva_cantidad = validarEntero("Error, ingrese una cantidad valida (0 o mayor)")

            elemento["cantidad_disponible"] = nueva_cantidad
            
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            print(f'¡Stock de "{elemento["nombre"]}" actualizado a {nueva_cantidad}!')
            return
        
        contador_aux += 1

def buscar_herramienta():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    id_elemento = validarEntero("Ingrese el ID de la herramienta a buscar")
    
    for elemento in herramientas:
        if elemento["id"] == id_elemento:
            print(f"Resultado: {elemento['nombre']} Categoria: {elemento['categoria']} Valor: ${elemento['valor_estimado']}")
            return elemento
    print("No se encontro la herramienta.")
    return None