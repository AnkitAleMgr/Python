def isPalindrome(x: int) -> bool:
    x = str(x)
    if not x.isdigit():
        return False
    reverse = x[::-1]
    return True if reverse == x else False



isPalindrome(-140)