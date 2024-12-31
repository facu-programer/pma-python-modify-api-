import sys
import os
import importlib.util
from log import log as log2

log = log2()

def load_libs():
    def cargar_modulo(nombre_archivo, directorio):
        """Carga un módulo dinámicamente y lo registra una sola vez."""
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        nombre_modulo = nombre_archivo.replace(".py", "")

        # Evita recargar el mismo módulo
        if nombre_modulo in sys.modules:
            return

        try:
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
            mi_modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mi_modulo)
            sys.modules[nombre_modulo] = mi_modulo
            log.registry(f"Dependencia '{nombre_modulo}' cargada correctamente.")
        except Exception as e:
            log.registry(f"Error al cargar la dependencia '{nombre_modulo}': {e}")

    # Obtén el directorio base del script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define los directorios donde buscar módulos
    directorios = [f"{current_directory}/libs"]

    modulos_cargados = set()  # Para evitar duplicados

    for directorio in directorios:
        if not os.path.exists(directorio):
            log.registry(f"El directorio '{directorio}' no existe. Saltando...")
            continue

        # Lista archivos .py en el directorio
        archivos = [archivo for archivo in os.listdir(directorio)
                    if os.path.isfile(os.path.join(directorio, archivo)) and archivo.endswith(".py")]

        for archivo in archivos:
            if archivo not in modulos_cargados:
                cargar_modulo(archivo, directorio)
                modulos_cargados.add(archivo)
    cargar_modulo("log.py", current_directory)
    cargar_modulo("dependencies.py", current_directory)