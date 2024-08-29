print("SJC23MCA-2017 : ANNA S")
print("Batch : MCA 2023-25")

import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x_cube_multiply=np.multiply(x,np.multiply(x,x))
x_cube_operator=x*x*x
x_cube_power=np.power(x,3)
x_cube_double_star=x**3
identity_matrix=np.identity(x.shape[0])
x_power_2=np.power(x,2)
x_power_3=np.power(x,3)
x_power_4=np.power(x,4)

print("Original Matrix x:",x)
print("Cubed Matrix (Method 1 - multiply()):",x_cube_multiply)
print("Cubed Matrix (Method 2 - * operator):",x_cube_operator)
print("Cubed Matrix (Method 3 - power()):",x_cube_power)
print("Cubed Matrix (Method 4 - ** operator):",x_cube_double_star)
print("Identity Matrix:",identity_matrix)
print("Matrix to Different Powers:")
print("x^2:",x_power_2)
print("X^3:",x_power_3)
print("X^4:",x_power_4)

