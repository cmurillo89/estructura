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