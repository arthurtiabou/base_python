x= -3 
print(abs(x)) # Affiche la valeur absolue de x, qui est 3

list_1 = [1, 2, 3, 4, 5]
print(sum(list_1)) # Affiche la somme de tous les éléments de list_1
print(max(list_1)) # Affiche le maximum de list_1, qui est 5
print(min(list_1)) # Affiche le minimum de list_1, qui est
print(len(list_1)) # Affiche la longueur de list_1, qui est 5

x = 5
type_x = type(x) # Récupère le type de x, qui est <class 'int'>
print(type_x)
x= str(x) # Convertit x en une chaîne de caractères
print(x) # Affiche la valeur de x, qui est "5"

pays = "Cameroun"

message = f"Le {pays} est mon beau pays !"
print(message) # Affiche le message formaté avec la variable pays

f = open("file.txt", "w") # Ouvre un fichier en mode écriture
f.write("Bonjour, ceci est un message dans le fichier.") # Écrit une chaîne de caractères dans le fichier
f.close() # Ferme le fichier

with open("file.txt", "r") as f: # Ouvre le fichier en mode lecture
    content = f.read() # Lit le contenu du fichier et le stocke dans la variable content
    print(content) # Affiche le contenu du fichier
