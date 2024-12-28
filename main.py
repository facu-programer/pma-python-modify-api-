from log import log as log2
log2().registry("log importado")
from fdi import fdi
log2().registry("fdi impotado")
from libs import load_libs
log2().registry("load_libs importado")

log = log2()
log.registry("pma iniciado")

load_libs()
class pma:
  def __init__(self):
    self.api = {}
    self.inyecciones_hechas = {}
  def inyectar(self, ruta, code, line):
    self.inyecciones_hechas[line] = len(code.split("\n")) - 1
    nombre = f"proyect/{ruta}.py"
    try:
      func_inyecciones = self.api[nombre]
      func_inyecciones[line] = code
      self.api[nombre] = func_inyecciones
    except KeyError:
      self.api[nombre] = {line: code}
  def ejecutar(self, ruta, params):
    with open(f"proyect/{ruta}.py", "r") as f:
      code = f.read()
    inyecciones = self.api[f"proyect/{ruta}.py"]
    return fdi(code, inyecciones, params, self.inyecciones_hechas)()

"""pda2 = pma()
pda2.inyectar("ejemplo", "  print('hola mundo!')", 1)
pda2.inyectar("ejemplo", "  print('chau mundo!')", 2)
print(pda2.ejecutar("ejemplo", []))"""