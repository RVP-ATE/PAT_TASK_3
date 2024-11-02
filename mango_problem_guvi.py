def min_difference_mangoes(bags, M):
    # Sort the bags
    bags.sort()

    # Initialize minimum difference to a large number
    min_diff = float('inf')

    # Iterate through the sorted bags
    for i in range(len(bags) - M + 1):
        # Calculate the difference between the max and min in the current window
        current_diff = bags[i + M - 1] - bags[i]
        # Update the minimum difference if the current one is smaller
        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff


# just as example to check whether the above program is correct or not
bags = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
M = 16
# Number of students
result = min_difference_mangoes(bags, M)

print(f"The minimum difference between the maximum and minimum mangoes in the bags is: {result}")



