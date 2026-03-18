liste_1 = [1, 2, 3, 4, 5]
city = ["Paris", "Londres", "New York", "Tokyo"]
country = ["France", "Royaume-Uni", "États-Unis", "Japon"]

tuple = (1, 2, 3, 4, 5)
print(tuple)

liste_1.append(6)

city.append("Berlin") # Ajoute "Berlin" à la liste city
count = city.count("Paris") # Compte le nombre d'occurrences de "Paris" dans la liste 

if "yaounde" in city:
    print("Yaoundé est dans la liste city.")
else:
    print("Yaoundé n'est pas dans la liste city.")

for i in city:
    print(i)


for i, v in enumerate(city):
    print(f"Index: {i}, Value: {v}")

for a, b in zip(city, country):
    print(f"City: {a}, Country: {b}")