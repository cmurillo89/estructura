# Una función que solicite la carga del día, mes y año y almacene dichos datos en una tupla que luego debe retornar. La segunda función debe recibir una tupla con la fecha y mostrarla en la consola.

# def cargar_fecha():
#     dd = int(input("Ingrese número de día: "))
#     mm = int(input("Ingrese número de mes: "))
#     aa = int(input("Ingrese número de año: "))
#     return (dd,mm,aa)

# def imprimir_fecha(fecha):
#     print(fecha[0],fecha[1],fecha[2],sep="/")

# # Bloque principal

# fecha = cargar_fecha()

# imprimir_fecha(fecha)

# Empaquetado y desempaquetado de tuplas.
# Podemos generar una tupla asignando a unavariable un conjunto de variables o valores separados por coma:

x=10
y=30
punto = (x,y)

print(punto)

# Tenemos 3 variables de las cuales vamos a desempaquetar:
print("--------------------------------------")

fecha = (25, "diciembre", 2023)
print(fecha)

dd,mm,aa = fecha
print("Día ",dd)
print("Mes ",mm)
print("Año: ",aa)

