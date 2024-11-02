# Defining the prime number (Identify the prime numbers using mathematical formula)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Given set of prime numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in numbers if is_prime(num)]
# Count of identified prime numbers
count_of_primes = len(prime_numbers)
#Printing the results
print("Count of prime numbers:", count_of_primes)
print("List of prime numbers:", prime_numbers)




