# doing by the python liberty
# def isPalindrome(s: str) -> bool:
#     new_s = ''
#     for ele in s:
#         char = ele.lower()
#         if char >= 'a' and char <= 'z' or (char >= '0' and char <= '9'):
#             new_s += char
#     return new_s == new_s[::-1]


# more traditional method, two pointer approach
def isPalindrome(s: str) -> bool:
    new_s = ''
    for ele in s:
        char = ele.lower()
        if char >= 'a' and char <= 'z' or (char >= '0' and char <= '9'):
            new_s += char
    if len(new_s) == 0: return False
    i = 0
    j = len(new_s)-1
    print(new_s)

    while i != j:
        if new_s[i] != new_s[j]:
            return False
        i +=1
        j -=1
    return True

print(isPalindrome("race a car"))
