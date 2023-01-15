# NumPy assignment

# Q1 - write a function only_odd_numbers(v) that receives a vector v (as a list) and returns a numpy array of only the odd numbers from v.

import numpy as np
def only_odd_numbers(v):
    v = np.array(v)
    mask = (v % 2 == 1)
    
    return (v[mask])

# Q2 - write a function replace_all_negative(v) that replaces all the negative values in v (that is a list of integers) whit the value 0. The function returns the updated array. Use numpy

import numpy as np
def replace_all_negative(v):
    v = np.array(v)
    is_positive = v > 0
    v[~is_positive] = 0
    return(v)

# Q3 - Write a function parallel_matris(mat) that receives a matrix (as a list) and returns true if its columns are parallel vectors, else returns false.

import numpy as np
def parallel_matris(mat):
    mat = np.array(mat)
    mat_size = mat.shape
    v1 = mat[:, 0]
    for i in range(1, mat_size[1]):
        vi = mat[:, i]
        if not (v1/vi == (v1/vi)[0]).all():
            return False
    return True


# Q4 - write a function reverse_matrix_columns(mat) that that takes a matrix mat as a list and returns reversed columns matrix. use numpy to solve it in one line.

import numpy as np
def reverse_matrix_columns(mat):
    return np.flip(mat, 1)

# Q5 - Implement a function called mat_transpose(mat) which receives a valid matrix called mat (as a list) and returns a new matrix which is the transpose of matrix mat. Matrix transposition consists in switching the rows and columns of the matrix. The function will receive a matrix with n rows and m columns, and will return a matrix with m rows and n columns that contains at position (i,j) the item that was contained at position (j,i) of the original matrix. 

import numpy as np
def mat_transpose(mat):
    return np.transpose(np.array(mat))
