def find_duplicates_nested_loop(l: list) -> list:
    duplicates = set() # Using a set here will keep us from adding the duplicates more than once

    # Starting with the first number 
    for i in range(len(l)):
        # Go through every number after the current number
        for j in range(i+1, len(l)):
            # Check for duplicates
            if (l[i] == l[j]):
                duplicates.add(l[i])
    
    return list(duplicates)

def find_duplicates_dictionary(l: list) -> list:
    duplicates = {}
    for num in l:
        duplicates[num] = duplicates.get(num, 0) + 1
        # I found the above code via google -> stack overflow TRUST
        # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
        # I was getting errors trying to access keys that didn't exist so I was looking on google for how to do that

    list_duplicates = []
    for key, value in duplicates.items():
        if value > 1:
            list_duplicates.append(key)

    return list_duplicates

# In Python, if __name__ == "__main__" is a conditional check that determines whether 
# a Python file is being run as the main program or imported as a module into another 
# script.
if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))
    print("\nSample 1:", find_duplicates_dictionary(sample1))
    print("Sample 2:", find_duplicates_dictionary(sample2))
    print("Sample 3:", find_duplicates_dictionary(sample3))
    print("Sample 4:", find_duplicates_dictionary(sample4))