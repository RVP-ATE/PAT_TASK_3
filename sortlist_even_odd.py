# List provided from the question
numbers = [10, 507, 22, 37, 10, 999, 87, 351]

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the list and separate even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Output the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)