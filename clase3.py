# Uso de string 

# Dividir cadenas

new_users= "Christopher Murillo Gómez"

user_name = new_users.split()

print(user_name)

user = "Chris,36,M,Ing"

user_1 = user.split(",")

print(user_1)

# Actualizaciones de cadenas

special = "Today's special is pasta"

new_special = special.replace("pasta","pizza")

print(new_special)

value = "44,000"

fixed_value = value.replace(",",".")

print(fixed_value)


# Casting de variables

# Hay varios tipos de datos básicos en Python: cadenas, enteros, flotantes y booleanos. La función type() devuelve el tipos de valor

print(type("hello"))
print(type(10.5))
print(type(10))
print(type(True))

# A veces necesitamos cambiar valores de un tipo a otro. Esto se llama conversión de tipos

age = "17"
if int(age) < 18:
    print("You are too young!")


position = 3
update = "You are now number " + str(position) + " in the queue."
print(update)

price = 9.99
print(int(price))


member = True
value = int(member)
print(value)

# Python tambiénproporciona las funciones list(), dict(), set() y tuple() para la conversion de tipos de estructuras de datos compuestas adecuadas.

choices = ["pizza", "kebab", "burger", "pizza"]
unique = set(choices)
print(unique)

# FUNCIONES
# Funciones de código para haer que el código sea reutilizable y más fácil de leer y usar.

# Reutilización de código con funciones.

def greet_user():
    print("Good morning Esteban")
    print("Welcome back")

greet_user()

# Creación de parámetros

def greet_ron():
    name = "Ron"
    print(f"Hello, {name}")

greet_ron()


def greet(name):
    print(f"Hello, {name}")

greet("Chris")


def user_status(status):
    username = "Chris"
    print(f"{username} is {status}")

user_status("active")

def double_number(number):
    result = number * 2
    print(result)

double_number(5)

# Valores devueltos
# Para devolver algo de una función, agregamos la palabra clave de RETURN seguida del valor a devolver, como aquí.

def age_label(age):
    label = "User age: " + age
    return label

edad = age_label("18")
print(edad)


def half_twice(number):
    half = number/2
    half_again = half / 2
    return half_again

result = half_twice(12)
print(result)

# Uso de múltiples parámetros

def show_winner(first, second, third):
    print("First place: "+first)
    print("Second place: "+ second)
    print("Third place: "+third)

show_winner("Esteban","Chris","Paul")

def create_email(name, year):
    return name + year + "@hutmail.com"

email = create_email("cmurillo","1989")

print(email)

# Vamos a aprender a comprender las funciones:
# Funciones de nomenclatura:

def get_final_price(price, tax):
    return price + tax
price = get_final_price(30,1.5)
print(price)

# Alcance de las funciones:
# Las variables creadas dentro de una función tienen un ALCANCE LOCAL, como por ejemplo:

def add_bonus(salary):
    bonus = 100
    print(salary+bonus)

add_bonus(1900)

# Alcance global de las funciones

# shipping = 10

# def calculate_total(cart):
#     print(cart + shipping)

# print(shipping)
# calculate_total(54)

# Añadir condiciones en funciones

def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart+10}")
    else:
        print(f"Total:{cart}")

add_shipping(45)
add_shipping(200)

# TAMBIEN PODEMOS ANIDAR DECLARACIONES ELIF COMO ESTA QUE ENCONTRAMOS EN EL SIGUIENTE EJEMPLO

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")

calculate("*",40,30)

# Cualquier tipo de valor puede servir como entrada o 
# salida de una función. De esta manera las funciones pueden hacer uso de las listas

def is_multiplayer(players):
    print(len(players) == 2)

players = ["Freddy","Paul"]
is_multiplayer(players)

# FUNCIONES CON BUCLES
# Las funciones nos ayudan a reutilizar los bucles permitiéndonos cambiar el número de
# repeticiones o la lista por la que estamos iterando.

def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1

onboard_passengers(15)

def display_progress(total_files):
    for i in range(total_files):
        i += 1
        print(f"Downloading file {i} out of {total_files}")

display_progress(3)

# La utilización de un bucle que itera a través de una lista.

def halve_price(cart):
    for price in cart:
        print(f"New price: {price/2}")

cart_list = [5, 20, 8]
halve_price(cart_list)

def display_players(team):
    number = 1
    for name in team:
        print(f"Player {number}: {name}")
        number += 1

team1 = ["Kim", "lee"]
team2 = ["Meg", "Jo"]

display_players(team2)
