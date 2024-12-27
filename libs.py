from log import log as log2
log = log2()
import sys
import os
import importlib.util

def load_libs():
    # Obtén el directorio del archivo en ejecución
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define el directorio donde están los módulos
    directorio = f"{current_directory}/libs"
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return

    # Lista todos los archivos en el directorio
    archivos = os.listdir(directorio)
    solo_archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(directorio, archivo)) and archivo.endswith(".py")]

    for archivo in solo_archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        nombre_modulo = archivo.replace(".py", "")

        # Cargar el módulo dinámicamente
        try:
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
            mi_modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mi_modulo)

            # Añadir el módulo a sys.modules
            sys.modules[nombre_modulo] = mi_modulo
            log.registry(f"dependencia: '{nombre_modulo}' cargada correctamente.")
        except Exception as e:
            print(f"Error al cargar la dependencia '{nombre_modulo}': {e}")
            log.registry(f"Error al cargar la dependencia '{nombre_modulo}': {e}")
        # Obtén el directorio del archivo en ejecución
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define el directorio donde están los módulos
    directorio = f"{current_directory}"
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        archivo = "log.py"
        ruta_archivo = os.path.join(directorio, archivo)
        nombre_modulo = archivo.replace(".py", "")

        # Cargar el módulo dinámicamente
        try:
            spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
            mi_modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mi_modulo)

            # Añadir el módulo a sys.modules
            sys.modules[nombre_modulo] = mi_modulo
            log.registry(f"dependencia: '{nombre_modulo}' cargada correctamente.")
        except Exception as e:
            print(f"Error al cargar la dependencia '{nombre_modulo}': {e}")
            log.registry(f"Error al cargar la dependencia '{nombre_modulo}': {e}")
            