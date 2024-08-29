number = int(input("Enter a number to check if its a perfect square or not:"))
if number <= 0:
    print("invalid input.please enter a positive integer.")
else:
    sum_of_divisors=0
    for i in range(1,number):
        if number % i== 0:
            sum_of_divisors  += i
    if sum_of_divisors == number:
        print(f"{number} is perfect number")
    else:
        print(f"{number} is not a perfect number")