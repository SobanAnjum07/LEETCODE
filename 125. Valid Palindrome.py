def isPalindrome(s: str) -> bool:
    new_s = ''
    for ele in s:
        char = ele.lower()
        if char >= 'a' and char <= 'z' or (char >= '0' and char <= '9'):
            new_s += char
    return new_s == new_s[::-1]
