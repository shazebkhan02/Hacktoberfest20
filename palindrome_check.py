# palindrome_check.py
# Check if a string is a palindrome

text = input("Enter a word: ").lower()

if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
