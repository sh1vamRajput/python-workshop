x=10
def modify_global():
    global x
    x=10
    modify_global()
    print(x)
    def couter_function():
        y=5
        def inner_function():
            nonlocal y
            inner_function
            print(y)
 