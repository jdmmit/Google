# Instala las librerías necesarias si no están presentes
import subprocess
import sys

def instalar_librerias():
    paquetes = ["numpy", "pandas", "matplotlib", "seaborn"]
    for paquete in paquetes:
        subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])

if __name__ == "__main__":
    instalar_librerias()
    print("Hola, mundo!")