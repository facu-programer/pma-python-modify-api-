**COMO USARLO:**
1. pon el proyecto que quieras editar en el directorio proyect
2. crea un nuevo archivo de python en el directorio principal
3. importa pma con **from main import pma**
4. inicializa pma con **init_pma = pma()**

**FUNCIONES:**

1. **pma.inyectar(ruta, codigo, linea)** sirve para inyectar codigo en un cierto archivo en una cierta linea, argumentos: ruta es la dirección del archivo en proyect, codigo el código a inyectar y linea la linea
2. **pma.ejecutar(ruta, parametros)** sirve para ejecutar un archivo, argumentos: ruta es la dirección del archivo en proyect, parametros son los argumentos del código

**ESTRUCTURA:**

1. el proyecto a editar va en proyect
2. los archivos deben tener solo una función, el código fuera de la función no sera ejecutado 
