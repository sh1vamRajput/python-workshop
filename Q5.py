#write a python script to check whether given key already exists in a dictionary.
d = {1:10,2:20, 3:30,4:40,5:50,6:60}
key2check=int(input("Enter the number"))
if key2check in d:
    print("key exist")
else:
    print("does not exist")