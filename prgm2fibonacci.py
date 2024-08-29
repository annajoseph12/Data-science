n=int(input("Enter the number of fibonacci numbers to print:"))
a=0
b=1
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c

