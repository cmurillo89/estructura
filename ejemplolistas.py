# Problema 1
# Definir una lista vacía y luego solicitar la entrada de 5 enteros por teclado y añadirlos a la lista. Luego imprime la lista generada.

# lista = []
# # disponemos un ciclo de 5 vueltas
# for x in range(5):
#     valor = int(input("Ingrese un valor entero: "))
#     lista.append(valor)

# # Imprimimos la lista
# print(lista)


# Problema 2
# Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.


lista2 = []

valor2 = int(input("Ingresar valir (0 para finalizar)"))

while valor2 != 0:
    lista2.append(valor2)
    valor2 = int(input("Ingresar valir (0 para finalizar)"))

print("Tamaño de la lista: ",len(lista2)," dígitos")
