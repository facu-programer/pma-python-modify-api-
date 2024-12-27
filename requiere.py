def requiere(lib: list):
  for e in lib:
    try:
      with open(f"libs/{e}" , "r"):
        pass
    except Exception:
      print(f"la dependencia {e} no existe")
      from log import log
      log2 = log()
      log2.registry(f"la dependencia {e} no existe")