def find_triplet_with_sum(nums, target_sum):
    nums.sort()  # Sort the list first
    n = len(nums)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target_sum:
                return (nums[i], nums[left], nums[right])  # Return the triplet
            elif current_sum < target_sum:
                left += 1  # Move left pointer to the right to increase the sum
            else:
                right -= 1  # Move right pointer to the left to decrease the sum

    return None  # If no triplet found


# set of values which include the triplet which gives sum 59
numbers = [10, 20, 30, 9]
value = 59
triplet = find_triplet_with_sum(numbers, value)

if triplet:
    print("Triplet found:", triplet)
else:
    print("No triplet found.")
