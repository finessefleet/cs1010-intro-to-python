def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

word = input("Enter a word or sentence: ")
if is_palindrome(word):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
