#write a python prgram to get a dictionary from an object's fields.
class Person:
   def __init__(self):
       self.name = 'John'
       self.age = 30

p = Person()
print(vars(p))