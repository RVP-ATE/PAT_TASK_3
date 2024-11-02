def first_non_repeating_element(nums):
    count = {}

    # Count occurrences of each number
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Find the first non-repeating element
    for num in nums:
        if count[num] == 1:
            return num

    return None  # If there is no non-repeating element


# just as example to check whether the above program is correct or not
numbers = [4, 5, 1, 2, 0, 4, 5, 1]
result = first_non_repeating_element(numbers)
print("First non-repeating element:", result)
