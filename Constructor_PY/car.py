cars = [
    "audi",
    "bmw",
    "mercedes"
]

print("Type of cars:", type(cars))

# add a new car
cars.append("ferrari")

# insert at a specific position
cars.insert(1, "tesla")

# check if a car exists
if "bmw" in cars:
    print("BMW is present in the list")

# remove a car
cars.remove("audi")

# sort the list
cars.sort()

# print cars using loop
print("Final car list:")
for car in cars:
    print(car)
