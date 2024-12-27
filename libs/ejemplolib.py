class ejemplolib:
  def saludar(self, nombre):
    import log as log2
    log = log2.log()
    print(f"hola {nombre}")
    log.registry(f"saludando a {nombre}")
  version = 1
