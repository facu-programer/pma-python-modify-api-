class log:
  def registry(self, data):
    try:
      with open("logs/log.log", "a") as f:
        from datetime import datetime
        fecha_actual = datetime.now().isoformat()
        f.write(f"\n[{fecha_actual}] {data}\n")
    except Exception:
      with open("logs/log.log", "w") as f:
        from datetime import datetime
        fecha_actual = datetime.now().isoformat()
        f.write(f"\n[{fecha_actual}] {data}\n")