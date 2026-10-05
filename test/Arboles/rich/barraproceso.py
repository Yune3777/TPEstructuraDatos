from rich.progress import track
import time


for i in track(range(100), description="Cargando..."):
     time.sleep(0.01)