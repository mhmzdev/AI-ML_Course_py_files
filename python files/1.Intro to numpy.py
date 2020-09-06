import numpy as np
# Numpy lecture

# Declaring 2D array using numpy
arr = np.array([[1,2,3,4,5,11,12],
				[5,6,7,8,9,13,14]])


# important functions regarding array in numpy

print("Dimension ", arr.ndim)	# dimension of array
print("Shape ",arr.shape) # shape of array (number of rows and columns)
print("Size in Memory ",arr.nbytes) # size of array in memory
print("Number of elements ",arr.size)	# number of elements


# Accessing array

# printing specific element print(array.[row, column])
print(arr[0,4])

# #printing a full row
print(arr[0, :])

# #printing a full column
print(arr[:, 0])

#getting some specific or fancy stuff print(array[startindex, endindex, stepsize])
print(arr[0, 1: -1: 2])

#identity matrix
print(np.identity(4))

#copying array
b = arr.copy()
# b[0, 2] = 100
print(arr) 	# it will not change
print(b)	# the only index mentioned with change will be changed here

#array addition
a = np.array([2,3,4])
print(a + 2)

#trignometric ftns
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(np.log(a))
print(np.exp(a))

# list lecture
lst = [1,2,3,4,5]
