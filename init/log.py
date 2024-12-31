import os
from datetime import datetime

class log:
    def registry(self, data):
        try:
            # Asegúrate de que el directorio exista
            os.makedirs("logs", exist_ok=True)

            with open("logs/log.log", "a") as f:
                fecha_actual = datetime.now().isoformat()
                f.write(f"\n[{fecha_actual}] {data}\n")
        except Exception as e:
            os.makedirs("logs", exist_ok=True)
            with open("logs/log.log", "w") as f:
                fecha_actual = datetime.now().isoformat()
                f.write(f"\n[{fecha_actual}] {data}\n")