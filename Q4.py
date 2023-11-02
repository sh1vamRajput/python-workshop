#Write a python program to sort a given dictionary by key.
#Hint: Use sorted()
#Input:
color_dict = {'red':'#FF0000',
              'green':'008000',
              'black':'000000',
              'white':'#FFFFFF'}


color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'FFFFFF'}
sorted_dict = dict(sorted(color_dict.items()))
print(sorted_dict)