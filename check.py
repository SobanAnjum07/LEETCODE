
def func(s, ind=0, cur='', res=None):
    
    if res is None:
        res = []
        
    if ind == len(s):
        res.append(cur)
        return
        
    func(s, ind+1, cur+s[ind], res)
    func(s, ind+1, cur, res)    
    return res


s =  "abc"
print(func(s))
    