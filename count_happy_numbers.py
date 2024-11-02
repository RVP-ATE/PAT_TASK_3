# Defining the happy numbers
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in numbers if is_happy(num)]
# Count the number of Happy numbers
count_of_happy_numbers = len(happy_numbers)
# Printing the results
print("Count of happy numbers:", count_of_happy_numbers)
print("List of happy numbers:", happy_numbers)
