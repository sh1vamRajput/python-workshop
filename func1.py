x=10
def my_function():
    print(x)
    
x=10 # x is a global variable
def my_function():
    print(x) # Accessing the global

    my_function()
