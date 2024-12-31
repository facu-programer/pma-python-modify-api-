
def fdi(code: str, inyecciones, inyecciones_echas): #funciones de inyeccion
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
    def func():
        return exec(code9, globals())
    return func
  def code3():
    return code2()
  return code3()