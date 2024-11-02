def find_minimum(sorted_list):
    if not sorted_list:
        return None
    return sorted_list[0]

# just as example to check whether the above program is correct or not
sorted_numbers = [1, 2, 3, 4, 5]  # A sorted list
minimum = find_minimum(sorted_numbers)
print("Minimum element:", minimum)