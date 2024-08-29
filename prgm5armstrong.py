for num in range(1, 1001):

    num_str = str(num)
    num_digits = len(num_str)

    sum_of_digits = 0
    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits

    if num == sum_of_digits:
        print(num)
