
'''
.########
.##......
.##......
.#######.
.......##
.##....##
..######.

'''

def check_palindrome(s):
    pass
    
    
def isPalindrome(s):
    return s == s[::-1]
    

def longest_palindrome(string):
    # string = input()
    starting = 0
    len_pal = 0
    
    for _ in range(len(string)):
        ending = len(string)
        
        for i in range(len(string)):
            
            if isPalindrome(string[starting:ending]) and len(string[starting:ending]) > 1 and len_pal < len(string[starting:ending]): 
                len_pal = len(string[starting:ending])
                ret_str = string[starting:ending]
            
            ending -=1
            
        starting += 1
        
    return ret_str
    
    

if __name__ == '__main__':
    s = 'kalaabcdcbaj'
    # s = 'abcdcba'
    print(longest_palindrome(s))
    pass
    
    
                
        

