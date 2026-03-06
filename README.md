# Programa de gestión de herramientas 🛠️❗
# Lenguaje de programación Python (▀̿Ĺ̯▀̿ ̿)
## ⚠️ Problematica: ⚠️
En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles.

La junta comunal de tu barrio ha decidido organizar este proceso mediante un programa de consola que registre las herramientas, los vecinos y los préstamos realizados. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas.
## 🪄🔮 Solución: ( ͡° ͜ʖ ͡°) 🪄🔮
Creación de una aplicación de registros de solicitudes de prestamos, prestamos y herramientas para la junta de acción comunal, para esto un admin deberá de estar al mando de la aplicación, el será el encargado de registrar el stock de las herramientas, de mirar las solicitudes y según estas aceptar las solicitudes y hacer el prestamo.
## 🔵👀 Estructura: ✍️(◔◡◔) 🔵👀
Este proyecto hace uso de funciones de validacion de datos y de funciones de json, a continuación verá las funciones y de lo que se encargan cada una:
### Validaciones:
#### 1. Validación de validar Menú:
```
def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None
```
Esta función se encarga de validar que el usuario elija una de las opciones desde la primera hasta la ultima.

#### 2. Validación de nombre:
```
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Nombre vacio")
        return False
    return True
```
Esta función se encarga de basicamente validar que el usuario ponga un caracter.

#### 3. Validación de entero:
```
def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None
```
Esta función se encarga de validar si lo que se el usuario puso es un entero.

#### 4. Validación de valor:
```
def validarValor(mensaje):
    valor = validarEntero(mensaje)
    
    while valor == None or valor < 0:
        print("Error: El valor debe ser un número positivo.")
        valor = validarEntero(mensaje)
        
    return valor
```
Esta función se encarga de validar que el número ingreado sea un número positivo.

#### 5. Validación de un entero con rango:
```
def validarEnteroConRango(mensaje, valor_minimo, valor_maximo):
    errores=True
    while(errores):
        try:
            dato=int(input(mensaje))
            while(dato<valor_minimo or dato>valor_maximo):
                dato=int(input('Error ', mensaje))
            errores=False
        except Exception as e:
            print('Error, se deben ingresar solo numeros')
        if errores==False:
            break
    return dato
```
Esta función se encarga de validar un número entero en un rango.

#### Funciones de Json:
```
import os
import json

def cargar(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar(nombre_archivo, datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos, archivo, indent=4)

def generar_id(lista):
    if not lista:
        return 1
    return lista[-1]["id"] + 1
```
Estas funciones se encargan de que las cargas a archivos .json funcionen.

### Ahora veremos el proyecto como tal: ＼（〇_ｏ）／
### 1. Simulación de inicio de sistema:
```
print("Iniciando sistema...")
time.sleep(1)
print("[##        ] 20%")
time.sleep(1)
print("[######    ] 60%")
time.sleep(1)
print("[##########] 100%")
time.sleep(0.5)
print("¡Carga completa!")

```
Esta parte es más que todo decorativa.
### 2. Menú princial y clave para cargarlo
```
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
```
En esta parte se hace la función del menú principal, este menú es el encargado de dar ingreso al menú para los usuarios y al menú del admin
```
contraseña=input('Ingrese la clave para cargar el menú principal: ')
if contraseña=='flo75689':
    menuMain()
else:
    print(' Acceso denegado, clave incorrecta')
```
En esta parte se le pide al usuario que digite la clave correcta para poder acceder al menú principal, si la contraseña es la correcta ("flo75689") el usuario podrá ingresar al menú, sino el sistema se cerrará de inmediato, como un sistema de seguridad.

Al final se llama la función para que todo pueda servir.
### Detro del menú principal: Menú de admin:
```
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
```
Utilizamos validar menú para que el admin entre al menú de registrar los usuarios, herramientas, los prestamos y para que pueda ver los reportes.

### Dentro del menú princimal: Menú de Usuario:
```
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
```
Utilizamos validar menú para que el usuario entre al menú de consultar el estado de las herramientas y el de poder crear una solicitud para que el admin la acepte y pueda tener su prestamo de herramienta.

### Dentro de los menús: Menú admin
```
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
```
#### Estas funciones basicamente hacen esto:

- Usuarios: Guardas, listas y borras solicitudes de la gente.
- Herramientas: Es el inventario. Aquí creas, buscas, borras y actualizas el stock o el estado de cada equipo.
- Préstamos: Controlas quién se lleva qué, ves la lista de lo que está afuera y marcas las devoluciones.
- Reportes: Te avisa qué herramientas se están acabando y cuáles son las que más pide la gente.

### Las funciones que hacen el proyecto funcionar:
Las funciones que hacen el proyecto funcionar se encuentran en los modulos gestionar_usuario.py, gestionar_herramientas.py, gestionar_prestamos.py y gestionar_reportes.py

Estas funciones estan basadas en las funciones de .json y cada una esta validada para que cada dato que se le pregunte al admin o usuario tenga que ser el dato necesitado para que quede la información guardadas en el json.

## Para que tengan una idea de como funcionan en mi proyecto las funciones:

### Tomemos como ejemplo gestion_herramientas:

Este módulo proporciona una interfaz de línea de comandos para administrar un inventario de herramientas. Los datos se almacenan de forma persistente en un archivo JSON, garantizando que la información se mantenga actualizada entre sesiones.

## Funcionalidades Principales:

### 1. Gestión de Registros: (Crear y Eliminar)
- guardar_herramienta: Es el punto de entrada para nuevos equipos. Solicita nombre, categoría, cantidad, estado y valor. Valida que los datos sean correctos, genera un ID único automáticamente y guarda la información en herramientas.json.
- eliminar_herramienta: Permite dar de baja una herramienta del sistema mediante su ID. Incluye una validación para confirmar la existencia del registro antes de proceder.

### 2. Visualización y Búsqueda: (Leer)
- listar_herramientas: Despliega en consola un listado completo de todas las herramientas registradas, mostrando ID, nombre, stock y estado actual.
- buscar_herramienta: Localiza una herramienta específica por su ID y muestra sus detalles principales (nombre, categoría y valor). Es ideal para consultas rápidas.

### 3. Actualizaciones: (Editar)
- actualizar_estado_herramienta: Permite cambiar la situación operativa de una herramienta (ej. pasar de "Activa" a "En reparación") buscando por ID.
- actualizar_stock_herramienta`**: Especializada en la gestión de inventario. Permite modificar exclusivamente la cantidad disponible, validando que el nuevo stock no sea negativo.

## ⚙️ Estructura de Datos: (´▽`ʃ♡ƪ) ⚙️
En esta parte del codigo se hace la "tabla que va en el archivo .json:"
```
    nueva_herramienta = {
        "id": generar_id(herramientas),
        "nombre": nombre,
        "categoria": categoria,
        "cantidad_disponible": cantidad,
        "estado": estado,
        "valor_estimado": valor_estimado
    }
```
Cada herramienta se registra con los siguientes atributos:

| Atributo | Descripción |
| ---- | ---- |
| `id` | Generado automáticamente por la función genarar_id. |
| `nombre` | Nombre de la herramienta. |
| `categoria` | Categoria a la que pertenece. |
| `cantidad_disponible`| Stock |
| `estado` | 1: Activa | 2: En reparación | 3: Fuera de servicio. |
| `valor_estimado` | El valor del prestamo. |

Y basicamente así funcionan las demas partes del proyecto.

# Información de contacto: 🧑🏻‍🦱
## 🔵🔵 Autor: (￣︶￣*) 🔵🔵

Resbaloso

## 🔵🔵 Contacto: （づ￣3￣）づ╭～ 🔵🔵

juansetoscano@gmail.com

░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░
░░████████████░░░█████████████████░░░░░░