def most_frequent(string):
    # create an empty dictionary to store letter counts
    letter_count = {}

    # loop through each character in the string
    for char in string:
        # if the character is not already in the dictionary, add it and set the count to 1
        if char not in letter_count:
            letter_count[char] = 1
        # if the character is already in the dictionary, increment the count
        else:
            letter_count[char] += 1

    # sort the dictionary by value (i.e. count) in descending order
    sorted_letters = sorted(letter_count, key=letter_count.get, reverse=True)

    # print the sorted letters and their counts
    for letter in sorted_letters:
        print(f"{letter}: {letter_count[letter]}")

# example usage:
most_frequent("Mississippi")
