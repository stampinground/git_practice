"""
Ask the user for a string and print out whether
this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

test_string = input("Please enter a word to check if it is a palindrome: ")

def string_check(test_string):
    if test_string == test_string[::-1]:
        print (test_string + " is a palindrome!")
    else:
        print (test_string + " is not a palindrome")

string_check(test_string)
