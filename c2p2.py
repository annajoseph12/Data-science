print("SJC23MCA-2017 : ANNA S")
print("Batch : MCA 2023-25")

import numpy as np
arr_2d = np.array([ [1+2j, 3+4j, 5+6j], [7+8j,9+10j,11+12j] ],dtype=complex)
print("2d-Array")
print(arr_2d)
rows,columns=arr_2d.shape
print("number of rows :",rows)
print("number of columns:",columns)
dimensions=arr_2d.ndim
print("dimension of array:",dimensions)
reshaped_array=arr_2d.reshape(3,2)
print("Reshaped array:",reshaped_array)