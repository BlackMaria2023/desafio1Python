precio = float(input("ingrese el precio de suscripcion"))
usuarios = int(input("ingrese el numero de usuarios"))
gastos = float(input("ingrese los gastos totales"))

utilidades = precio * usuarios - gastos

print(f"las utilidades totales son : {utilidades}") 