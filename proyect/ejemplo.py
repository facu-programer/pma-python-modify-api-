def ejemplo():
  import log as log2
  from dependencies import dependencies
  dependencies().requiere({"ejemplolib": 2})
  log = log2.log()
  log.registry("ejemplo iniciado")
  from ejemplolib import ejemplolib
  ejemplo = ejemplolib()
  ejemplolib().saludar("Facundo!")
  return "hola mundo!"