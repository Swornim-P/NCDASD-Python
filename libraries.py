import numpy as np

# x = 4.0
# print(np.sqrt(x))
# print(np.cbrt(8.0))
# print(np.sin(30))
# print(np.abs(-3))


# import numpy as np
a=np.array(range(20))
print(a)
x=np.reshape(a, (4,5))    #Reshapes the linear array into the matrix of the entered row and columns
print(x)

#Transposing
print(x.T)
#x=np.reshape((20))



print(np.sum(x))
print(np.sum(x, axis = 0))
print(np.sum(x, axis = 1))
print(x[0])
print(x[1])
print(x[2])

print(x[:, 0])    #THis represents to print all rows and first columns

print(x[:, 1])  #all rows and second columns
