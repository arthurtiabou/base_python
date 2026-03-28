dictionnary = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dictionnary)

traduction = {"cat": "chat", "dog": "chien", "house": "maison"}
print(traduction["cat"]) # Affiche "chat"

traduction["car"] = "voiture" # Ajoute une nouvelle paire clé-valeur au dictionnaire
print(traduction)

print(traduction.get("snake", "Valeur par défaut")) # Affiche "chien"

animal = traduction.pop("dog") # Supprime la clé "dog" et retourne sa valeur
print(animal) # Affiche "chien"