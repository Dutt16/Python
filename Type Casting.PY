name = ("Penguin")
age = 15
is_student = True
weight = 38.5

print("Name:", name)
print("Data Type of Name is:", type(name))

print("Age:", age)
print("Data Type of Age is", type(age))

print("is_student:", is_student)
print("Data Type of Student is", type(is_student))

print("Weight:", weight)
print("Data Type of Weight is", type(weight))

print("\n After Type Casting...")
age = str(age)

print("\n Data Type of Age is", type(age))
print(age)

print("\n After Type Casting...")
weight = int(weight)

print("\n Data Type of Weight is", type(weight))
print(weight)