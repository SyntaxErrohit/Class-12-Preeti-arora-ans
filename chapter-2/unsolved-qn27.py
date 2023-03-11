from tabnanny import check


def check_palind(string):
    s = string.replace(" ", "")
    if s[::-1] == s:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")

check_palind("malayalam")
check_palind("nurses run")