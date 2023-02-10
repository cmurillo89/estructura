# last_name = "Murillo"
# name = "Christopher"
# print(name+" "+last_name)


# Diferentes maneras de expresar variables
# name = "Christopher"
# id = 113990099
# money = 0.02
# turn_on = True

# print("Load Data")
# status = False
# print(status)

# subscribed = True
# print(subscribed)

# Ejemplo de un interruptor
# is_day = True
# lights_on = not is_day

# print("Daytime?")
# print(is_day)

# print("Lights on?")
# print(lights_on)


# Código de ventas y stock
# stock = 600
# jeans_sold = 500
# target = 500

# target_hit = jeans_sold == target
# print("hit jeans sale target: ")
# print(target_hit)

# current_stock = stock - jeans_sold
# in_stock = current_stock != 0
# print("Jeans in stock: ")
# print(in_stock)


# Comparación de números y ejemplos

# result = 1 <= 15
# print (result)

# min = 5
# max = 10
# result = min <= max
# print(result)

# battery_level = 20
# low = battery_level <= 14
# print("Low battery: ")
# print(low)

# Comparaciones de cadenas de texto

# print("online" == "online")
# print("online" != "offline")

# Medidor de frecuencia cardiaca

# heart_rate = 150

# too_low = heart_rate < 60
# too_high = heart_rate > 100

# print("Heart rate low: ")
# print(too_low)

# print("Heart rate high: ")
# print(too_high)




# Cadenas de formato
# new_messages = 5
# print(f"{new_messages} new messages")

# new = 5
# read = 2
# print(f"{new-read} unread messages")

# print(f"{5} new messages and {2} friend request")

# Vamos a aprender condicionales

# is_charged = False
# if is_charged:
#     print("Charged")
# print("Low Battery")

# available = False
# if available:
#     print("1 in sotck")
# else:
#     print("Out of stock")

# hour = 21

# if hour < 12:
#     print("Good morning")
# elif hour < 17:
#     print("Good afternoon")
# else:
#     print("Good night")




ride_type = "Black"
credits = 4

ride_price = 0
final_price = 0

if ride_type == "DooberX":
    ride_price = 20.5
elif ride_type == "Black":
    ride_price = 37.9
else:
    ride_price = 18.7

print("Ride price: ")
print(ride_price)

if credits > 0:
    final_price = ride_price - credits

print("Final price: ")
print(final_price)