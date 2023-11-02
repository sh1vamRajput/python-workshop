#creating a dictionary:
student = {
    "name":"Alice",
    "age":25,
    "grade":"A"
}
print(student)

#Accessing Dictionary values:
name = student["name"]
age = student["age"]
print("name")
print("age")
#Modifying Dictionary values:
student["age"] = 26
#Addinge a new key-value pair
student["city"]="New York"


#Iterating Through a Dictionary:
for key , value in student.item():
    print(f"{key}:{value}")
#cheaking if a key Exist:
if "age" in student:
    print("age exist is the dictionary")
for value in student.values():
    print(f"(values)")

for value in student.key():
    print(f"(values)")
squares1 = {num: num**2 for num in range(1,5)}
print(squares1)

squares2 = {num: num**2 for num in range(1,6)}
print(squares2)
