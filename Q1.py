#write a python script to genrate and print a dictionary that contains a number(between1 and n) in the from (x,x*x).
#SyntaxErrorample Dictionary(n=5):
#Expected output:{1: 1,2: 4,3: 9,4: 16,5: 25}


def generate_dict(number):
   d = {}
   for i in range(1, number+1):
       d[i] = i ** 2
   return d

print(generate_dict(5))