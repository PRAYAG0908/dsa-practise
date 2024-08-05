def check_palindrome(s):
    if s == s[::-1]:
        print("String Is Palindrome")
    else:
        print("Not A Palindrome String")

s = "malayalam"
check_palindrome(s)