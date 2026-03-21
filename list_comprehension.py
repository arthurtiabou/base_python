import time


list_com = [[i for i in range(3)] for j in range(3)]
print(list_com)

start_time = time.time()
list_com = [i**2 for i in range(1000000)]
end_time = time.time()

last_name = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
first_name = ["John", "Jane", "Michael", "Emily", "David"]

full_name = [f"{first} {last}" for first, last in zip(first_name, last_name)]

duree_1 = end_time - start_time
print(f"Time taken: {duree_1}")

start_time = time.time()
list_com = []

for i in range(1000000):
    list_com.append(i**2)

end_time = time.time()
duree_2 = end_time - start_time

print(f"Time taken: {duree_2}")
print(f"List comprehension is {duree_2/duree_1:.2f} times faster than the for loop.")