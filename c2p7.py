print("SJC23MCA-2017 : ANNA S")
print("Batch : MCA 2023-25")

import numpy as np
matrix1=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
matrix_sum=matrix1+matrix2
matrix_diff=matrix1-matrix2
matrix_product=matrix1*matrix2
matrix_divide=matrix1/matrix2
matrix_multiply=np.dot(matrix1,matrix2)
matrix1_transpose=np.dot(matrix1,matrix2)
diagonal_sum=np.trace(matrix1)
print("matrix1:\n",matrix1)
print("matrix2:\n",matrix2)
print("matrix sum:",matrix_sum)
print("matrix_difference:\n",matrix_diff)
print("matrix element-wise product:\n",matrix_product)
print("matrix element-wise division:\n",matrix_divide)
print("matrix multiplication:\n",matrix_multiply)
print("transpose of matrix1:\n",matrix1_transpose)
print("sum of diagonal elements of matrix1:",diagonal_sum)