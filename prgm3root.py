import math

a = float(input("Enter the coefficient of a:"))
b = float(input("Enter the coefficient of b:"))
c = float(input("Enter the coefficient of c:"))
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("no real roots")
else:
    sqrt_discriminant=math.sqrt(discriminant)
    root1 = (-b+sqrt_discriminant)/(2*a)
    root2 = (-b-sqrt_discriminant)/(2*a)
    root1_rounded = round(root1, 2)
    root2_rounded = round(root2, 2)
    print(f"root1:{root1_rounded}")
    print(f"root2:{root2_rounded}")