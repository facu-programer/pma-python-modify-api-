como usarlo:
1. pon el proyecto que quieras editar en el directorio proyect
2. crea un nuevo archivo de python en el directorio principal
3. importa pma con **from main import pma**
4. inicializa pma con **init_pma = pma()**
5. **FUNCIONES:**
1. **pma.inyectar(ruta, codigo, linea)** sirve para inyectar codigo en un cierto archivo en una cierta linea, argumentos: ruta es la dirección del archivo en proyect, codigo el código a inyectar y linea la linea
2. **pma.interceptar(ruta, nombre, codigo)** sirve para interceptar una función al ser llamada, argumentos: ruta es la dirección del archivo en proyect, nombre es el nombre de la función a ser interceptada, código es el código a ser ejecutado al interceptar la función
3. **pma.ejecutar(ruta, parametros)** sirve para ejecutar un archivo, argumentos: ruta es la dirección del archivo en proyect, parametros son los argumentos del código (versión 0.0.3 o menor en posterior no se usa)
