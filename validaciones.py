def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None
    
def nombre_valido(nombre):
    if nombre.strip()=="":
        print("Nombre vacio")
        return False
    return True

def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarValor(mensaje):
    valor = validarEntero(mensaje)
    
    while valor == None or valor < 0:
        print("Error: El valor debe ser un número positivo.")
        valor = validarEntero(mensaje)
        
    return valor

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

