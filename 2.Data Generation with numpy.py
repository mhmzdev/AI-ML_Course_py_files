import numpy as np

# gerneating array of all zeros
a = np.zeros((2,4))

# generating array of all ones
one = np.ones((3,3))

# generating array of any other number
otherNumberArray = np.full ((3,3), 5)

# generating full_like
otherArray = np.full_like(a, 2)

# generating random numbers
randomArray = np.random.rand(2, 3)		# uniform distribution ; numbers will be from 1-0

# generatin random numebers
normalDistributionArray = np.random.randn(3,2) # normal distribution ; numebers will be from -1 to +1

# random integers
randomInt = np.random.randint(0, 10, size=(3,3))

# identity matrix
identityArr = np.identity(10)

# matrix multiplication
mat1 = np.array([[1,2,3], [4,5,6]])
mat2 = np.array([[7,8,9],[2,3,4], [3,2,6]])		# same rule of matrix multiplication is implemented here i.e. column(1) == row(2)
# dot product is the most important concept in deep learning and neural networks
mulResult = np.dot(mat1, mat2)

# arranging the order
arr = np.arange(0, 10)
arr1 = np. arange(0, 11, 2) # 2 == stepsize

# linspace ; will get you evenly separate interval
linEx = np.linspace(0, 10, 3)		# this means you can divide 10 into three equal intervals i.e. 0 5 10

# min max etc
myArr = np.array([3,4,2,45,2,19,55,24,23])
# max element in array
myArr.max()			# same work for .min()
# argmax will return the index of max value
myArr.argmax()		# samw work for .argmin()

# shape
myArr.shape			# print it to see (row, columns)

# reshape
myArr.reshape(1,9)

# determinant
newArr = np.array([[1,2],[3,4]])		# determinant is taken only of square matrix
np.linalg.det(newArr)					# linalg ==> linear algebra, det ==> determinant

# standard deviation
np.std(newArr)

# variance
np.var(newArr)

###### FILE HANDLING IN PYTHON
file = np.genfromtxt('files/myFile.txt', delimiter=',')
# if we simply print it now, it will get us all float numbers, we need integers
# type casting in FILE
file = file.astype('int32')
print(file)




