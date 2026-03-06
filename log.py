import os
import json
from gestionarJson import cargar, guardar
from datetime import datetime

ARCHIVO_SOLICITUDES = "solicitudes.json"

def registrar_log(mensaje):
    solicitudes = cargar(ARCHIVO_SOLICITUDES)
    archivo_log = "logs.json"
    logs = cargar(archivo_log)
    nuevo_evento = {
        "id_log": len(logs) + 1,
        "fecha_hora": str(datetime.now()),
        "evento": mensaje
        }
    logs.append(nuevo_evento)
    guardar(archivo_log, logs)