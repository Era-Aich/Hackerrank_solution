# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:39:39 2025

@author: asus
"""

def modified_str(s, n):
    result = []  # To store the modified string
    num = []     # To store the numbers to move to the front
    i = 0

    while i < n:
        if i < n - 1 and s[i].islower() and s[i + 1].isupper():  # Check for lowercase followed by uppercase
            result.append(s[i + 1])  # Add the uppercase character
            result.append(s[i])      # Add the lowercase character
            result.append("*")       # Add '*'
            i += 2                   # Skip the next character since it's already processed
        elif s[i].isdigit():         # Check if the character is a digit
            num.append(s[i])         # Add the digit to the 'num' list
            result.append("0")       # Replace the digit with '0'
            i += 1
        else:
            result.append(s[i])      # Add the character as it is
            i += 1

    # Combine the numbers (moved to the front) with the modified string
    return ''.join(num) + ''.join(result)

# Example usage
s = input(" ")
n = len(s)
x = modified_str(s, n)
print(x)
