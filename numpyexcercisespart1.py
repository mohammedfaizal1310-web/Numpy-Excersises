# -*- coding: utf-8 -*-
"""NumpyExcercisespart1.ipynb


"""

#Import Numpy
import numpy as np

###print Numpy version
print("Numpy Version:", np.__version__)
np.show_config()

#create null vector size 10
null_vectors=np.zeros(10 , dtype=int)
print(null_vectors)

###Find memory size of an array
arr=np.array([1,0,1])
print(arr.size)
print(arr.itemsize)
print("memory size",arr.size*arr.itemsize)

##Create null vector of size 10 and 5th element is 1
vector=np.zeros(10)
vector[4]=1
print(vector)

###Reverse a vector
vector=[1,3,4,5,2]
reverse_vector=vector[::-1]
print(reverse_vector)

##print a range of vectors
vec=np.arange(10,49)
print(vec)

###create a 3X3 Matrices from 0 to 8
matrix=np.matrix([[0,1,2],[3,4,5],[6,7,8]])
print(matrix)

##Find indices of non-zero elements from [1,2,0,0,4,0]
v=[1,2,0,0,4,0]
index=np.nonzero(v)
print(index)

##create 3X3 Identity matrix
I=np.identity(3 , dtype=int)
print(I)

###create a 3X3X3 array with random numbers
a=np.random.rand(3,3,3)
print(a)

###create a 10X10 array with random values and find maximum and minimum values
array=np.random.rand(10,10)
print(array)
print("maximum value:",array.max())
print("minimum value:",array.min())

###create a random vector of size 30 and find mean
array=np.random.rand(30)
print(array)
print("mean",array.mean())

###Create 2D array with 1 on the border and 0 inside
arr=np.ones((5,5) ,dtype=int)
arr[1:-1,1:-1]=0
print(arr)

##How to add a border (filled with 0's) around an existing array
arr=np.ones((5,5), dtype=int)
bordered_arr=np.pad(arr,pad_width=1,mode='constant',constant_values=0)
print(bordered_arr)

0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1

## Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
matrix=np.zeros((5,5), dtype=int)
values=[1,2,3,4]
np.fill_diagonal(matrix[1:], values)
print (matrix)

#create a checkboard pattern
rows,cols=np.indices((8,8))
checkboard=(rows+cols)%2
print(checkboard)

##Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
arr=np.arange(6*7*8).reshape((6,7,8))
print(np.unravel_index(99,(6,7,8)))

###Create a checkerboard 8x8 matrix using the tile function
arr=np.tile(([0,1],[1,0]),(4,4))
print(arr)

###Normalize a 5x5 random matrix
z=np.random.rand(5,5)
zmin,zmax=z.min(),z.max()
z_norm=z-zmin/zmax-zmin
print(z_norm)

