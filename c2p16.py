print("SJC23MCA-2017 : ANNA S")
print("Batch : MCA 2023-25")

import numpy as np
A=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b=np.array([-3,5,-2])
x=np.linalg.solve(A,b)
print("Matrix A:",A)
print("Vector b",b)
print("Solution for x:",x)