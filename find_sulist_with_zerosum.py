def find_sublist_with_zero_sum(nums):
    cumulative_sum = 0
    sum_indices = {0: -1}  # Initialize with sum 0 at index -1

    for i, num in enumerate(nums):
        cumulative_sum += num

        if cumulative_sum in sum_indices:
            # If the cumulative sum has been seen before, we found a sublist
            start_index = sum_indices[cumulative_sum] + 1
            return nums[start_index:i + 1]  # Return the sublist

        # Store the index of the cumulative sum
        sum_indices[cumulative_sum] = i

    return None  # If no sublist found


# for the given number of list
numbers = [4, 2, -3, 1, 6]
sublist = find_sublist_with_zero_sum(numbers)

if sublist:
    print("Sublist with sum equal to zero:", sublist)
else:
    print("No sublist with sum equal to zero found.")
