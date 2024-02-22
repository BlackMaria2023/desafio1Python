precio = float(input("ingrese el precio de suscripcion"))
usuarios_normales = int(input("ingrese el numero de usuarios normales"))
usuarios_premium = int(input("ingrese el numero de usuarios premium"))
gastos = float(input("ingrese los gastos totales"))


utilidad_usuario_premium = precio * 1.5 * usuarios_premium
utilidades = (precio * usuarios_normales) + utilidad_usuario_premium - gastos

print(f"las utilidades totales son : {utilidades}") 