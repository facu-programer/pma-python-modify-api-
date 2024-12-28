
def fdi(code: str, inyecciones, params, inyecciones_echas): #funciones de inyeccion
  def code2():
    code_list = code.split("\n")
    for c, v in inyecciones.items():
      line = c
      for c2, v2 in inyecciones_echas.items():
        if c2 < c:
          line += v2
      code_list.insert(line, v)
      inyecciones_echas[c] = len(v.split("\n")) - 1
    code9 = "\n".join(code_list)
    exec(code9, globals())
    print(code9)
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