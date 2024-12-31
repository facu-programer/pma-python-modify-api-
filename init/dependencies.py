class dependencies:
  def requiere(self, lib: dict):
    from log import log
    log2 = log()
    for c, v in lib.items():
      try:
        with open(f"libs/{c}.py" , "r"):
          pass
      except Exception:
        print(f"la dependencia {c} no existe")
        
        log2.registry(f"la dependencia {c} no existe")
      try:
        exec(f"import {c}")
      except Exception:
        print(f"la dependencia {c} no se pudo importar") 
        log2.registry(f"la dependencia {c} no se pudo importar")
      try:
        exec(f"import {c}\n{c}.{c}().version")
      except Exception:
        print(f"la dependencia {c} no tiene una version")
        log2.registry(f"la dependencia {c} no tiene una version")
      exec(f"import {c}\nif {c}.{c}().version < {v}:\n  ver = False\nelse:\n  ver = True", globals())
      if not ver:
        error = f"la dependencia {c} no esta en la version {v}"
        print(error)
        log2.registry(error)
      
  def listar(self):
    from os import listdir
    from os.path import isfile, join
    import os
    current_directory = os.path.dirname(os.path.abspath(__file__))
    directorio = f"{current_directory}/libs"
    solo_archivos = [archivo for archivo in listdir(directorio) if isfile(join(directorio, archivo))]
    return solo_archivos