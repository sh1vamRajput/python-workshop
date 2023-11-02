#write a python script to print a dictionary where the keys are numbers between 1 and 15 (both incuded) and the values are the square of the keys.
#Sample Dictionary
# Step 1: Define the range of keys
keys = range(1, 16)

# Step 2: Use a dictionary comprehension to create the dictionary
squares_dict = {key: key**2 for key in keys}

# Step 3: Print the dictionary
print(squares_dict)
# Step 1: Define the range of keys
keys = range(1, 16)


