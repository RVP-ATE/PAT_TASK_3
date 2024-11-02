def sum_first_last_digit(n):
    # Converting the number to a string to access the digits
    n_str = str(n)

    # Get the first and last digits
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])

    return first_digit + last_digit

# Input the number to check the sum of first and last digit
number = input("Enter the number: ")
result = sum_first_last_digit(number)
#printing the result
print(f"The sum of the first and last digit of {number} is: {result}")
