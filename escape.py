import math


radio_km = float(input("ingrese el radio en kilometros: "))
gravedad = float(input("ingrese la constante gravedad: "))

radio_m = radio_km * 1000


velocidad_de_escape = math.sqrt(2 * gravedad * radio_m)



print(f"la velocidad de Escape es : {velocidad_de_escape} [m/s]")

 





