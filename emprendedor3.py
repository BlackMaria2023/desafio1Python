precio = int(input("ingrese el precio de suscripcion"))
usuarios = int(input("ingrese el numero de usuarios"))
gastos = int(input("ingrese los gastos totales"))
utilidades_año_anterior = int(input("ingrese las utilidades del año anterior"))


utilidades = (precio * usuarios - gastos) / utilidades_año_anterior
# Muestro sólo 2 decimales print(f'El resultado es {1/9:.2f}')
print(f"las utilidades totales son : {utilidades:.2f}") 

