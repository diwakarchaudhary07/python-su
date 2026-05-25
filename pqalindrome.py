# Palindrome Program in Python

text = input("Enter a string or number: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")