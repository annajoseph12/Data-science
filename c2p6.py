print("SJC23MCA-2017 : ANNA S")
print("Batch : MCA 2023-25")

import numpy as np
two_dimensional_array=np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16] ])
excluding_first_row=two_dimensional_array[1:]
excluding_last_column=two_dimensional_array[:, :-1]
column_1_2_in_row_2_3=two_dimensional_array[1:3,0:2]
column_2_3 = two_dimensional_array[:, 1:3]
elements_2_3_in_first_row=two_dimensional_array[0,1:3]
descending_order=two_dimensional_array.ravel()[::-1][4:11]
print("original 2D array:\n",two_dimensional_array)
print("Elements excluding the first row:\n",excluding_first_row)
print("elements excluding the last colum:\n",excluding_last_column)
print("elements of the 1st and 2nd column in the 2nd and 3rd row:\n",column_1_2_in_row_2_3)
print("elements of the 2nd and 3rd column:\n",column_2_3)
print("2nd nad 3rd element of the 1st row:\n",elements_2_3_in_first_row)
print("elements from indices 4 to  10 in descending order:\n",descending_order)