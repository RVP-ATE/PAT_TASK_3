def find_duplicates(list1, list2, list3):
    # Convert lists to sets to find common elements
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    # Find intersection of the three sets
    duplicates = set1.intersection(set2).intersection(set3)

    return list(duplicates)


# just as example to check whether the above program is correct or not
list1 = [12, 23, 56, 45, 56]
list2 = [45, 56, 67, 78]
list3 = [51, 89, 90, 56]

duplicates = find_duplicates(list1, list2, list3)
print("Duplicates:", duplicates)

