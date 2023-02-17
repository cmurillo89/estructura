# keep_going = True

# while keep_going == True:
#     print("and again")

#     keep_going = False

#     print("one more time")


# Controlar un bucle

# counter = 5

# while counter < 10:
#     print(counter)
#     counter += 1


# inter_shipping = True

# total = 50
# shipping_cost = 0

# if inter_shipping:
#     shipping_cost += 15
#     print("International base cost applied")

# if total <= 50:
#     shipping_cost += 20
# elif total <= 100:
#     shipping_cost += 15
# else:
#     shipping_cost  += 5

# print(f"Shipping cost: {shipping_cost}")


# account = 100
# interest_rate = 0.10
# years = 30

# print(f"Initial amount:{account}")

# counter = 1
# while counter <= years:
#     accrued_interest = account * interest_rate
#     account += accrued_interest
#     account += 100
#     print(f"Year {counter}: {account}")
#     counter += 1


# Creación y usos de listas o array

# age = [25,21,29,26,23,32]
# age[2] = 40
# print(age[2])

# todo = ["Read", "Workout", "Code"]
# print(todo)

# scores = [24, 23]
# scores.append(25)

# print(scores)

# users = ["john","hanna","Chris"]
# users.append("esteban")
# print(users)

# shopping = ["kiwis","pear","tometo"]
# shopping.insert(0,"lemon")
# shopping.insert(1,"choco")
# print(shopping)

# todo = ["Read", "Workout", "Code"]
# removed = todo.pop(1)
# print(todo)
# print(removed)




# final_scores = [17,22,34,13]
# for score in final_scores:
#     print(score)
#     print("-------")

# data_points = [99,99,99,99]
# for data in data_points:
#     print(data+1)





# users = []

# number_of_users = len(users)

# if number_of_users > 0:
#     print(f"online users: {number_of_users}")
# else:
#     print("Offline app")






# flavors = ["cinnamon","apple pie","acid"]
# print("New flavors: ")
# print(flavors)

# ratings = [4,2.5,3]
# print("Consumer ratings: ")
# print(ratings)

# passed = [True,False,True]
# print("Release:")
# print(passed)






# humidity_level = [87,83,89,88,87]

# humidity_level.insert(0,90)
# humidity_level.pop()
# print(humidity_level)




# Encontrar los min y max en las listas

# humidity_level = [87,83,107,88,66]
# min = min(humidity_level)
# max = max(humidity_level)
# sorted = sorted(humidity_level)
# sum = sum(humidity_level)
# print(max)
# print(min)
# print(sorted)
# print(sum)


# dataset1 = [1,2,3]
# dataset2 = [4,5]
# combined = dataset1 +  dataset2

# print(combined)






humidity_level = [87,83,107,88,66,87,87,107]
count = humidity_level.count(107)
print(count)

find = 81
if find in humidity_level:
    print(f"{find} se encuentra en la lista")
else:
    print(f"El {find} no se encuentra en la lista")