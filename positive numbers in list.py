def print_positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            print(num)

# Example usage:
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Positive numbers in list1:")
print_positive_numbers(list1)

print("Positive numbers in list2:")
print_positive_numbers(list2)
