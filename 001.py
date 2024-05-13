# import string
# from math import sqrt
# import numpy as np


# # for i in range (100000):
# #   print (i)


# # a=1
# # while a<=5000:
# #     print (a)
# #     a+=1

# # a=5
# # a+=5
# # a='12'
# # b=int(a)
# # print (b+5)

# a=1
# b=-5
# c=6

# r1=(-b +np.sqrt(b**2 -4*a*c))/(2*a)
# r2=(-b -np.sqrt(b**2 -4*a*c))/(2*a)

# print(f'The roots are {r1} and {r2}')

# mylist = []
# for i in range (10):
#     mylist.append(i)

# for items in mylist:
#     print(items)


# print(f'The length of mylist is: {len(mylist)}')



# import string
# a='ram shyam'
# b=a.split
# print(a.split(" "))
# print (a.count('m')) #counts the number of occurance of the given character in the string

# print('Ram is a \'superboy\'') #\ paxadi ko euta letter lai python le ignore garxa

# print(a.upper())




a = 12345
reversed = 0
while a>0:
    reversed = (reversed*10 + a%10)
    a = a//10
print(reversed)
