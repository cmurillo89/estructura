movies = ["Vertigo", "Chucky", 1958, 2019]

# LAS TUPLAS SON PARA AGRUPAR DATOS RELACIONADOS

vertigo_data = ("vertigo",1958)
print(vertigo_data)

user_data = ("cmurillo",113990099,"M")
print(user_data)

# Podemos almacenar tuplas en una lista como cualquier otro valor, 

movies_tupla = [("vertigo",1958),("Chuchy",2019),("Terminator", 1999)]

movies_tupla[2] = ("La sirenita", 2000)
favorite = movies_tupla[2]
print(movies_tupla)

len = len(movies_tupla[1])

print(len)

# Las tuplas son útiles porque nos permiten devolver múltiples valores de una función,
# como lo siguiente

def get_scores_datos(score_list):
    highest_score = max(score_list)
    lowest_score = min(score_list)
    return highest_score, lowest_score
scores = [31, 17, 80]
data = get_scores_datos(scores)
print(data)
highest = data[0]
smallest = data[1]

print(f"Smallest score: {smallest}")
print(f"Highest score: {highest}")




# Ordenamiento
def get_scores_datos(score_list):
    highest_score = sorted(score_list)
    return highest_score
scores = [31, 17, 80]
data = get_scores_datos(scores)
print(data)
first = data[0]
second = data[1]
third = data[2]

print(f"First: {first}")
print(f"Second: {second}")
print(f"Third: {third}")
