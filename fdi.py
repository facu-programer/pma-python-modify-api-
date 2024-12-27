
def fdi(code: str, inyecciones, params): #funciones de inyeccion
  def code2():
    code_list = code.split("\n")
    for c, v in inyecciones.items():
      code_list.insert(c, v)
    code9 = "\n".join(code_list)
    exec(code9, globals())
    def nombre(linea):
      nombre2 = ""
      if linea.startswith("def "):
        registrar = False
        for e in linea:
          if e == " ":
            registrar = True
          elif e == "(":
            registrar = False
            break
          elif registrar:
            nombre2 += e
        return nombre2
    name = nombre(code9.split("\n")[0])
    def func():
        return eval(f"{name}({', '.join(params)})", globals())
    return func
  def code3():
    return code2()
  return code3()