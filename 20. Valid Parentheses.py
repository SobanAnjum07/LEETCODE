
def isValid(s: str) -> bool:
    lst = list(s)
    stack = []
    map = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        ')': None,
        ']' : None,
        '}' : None
        }
    inp = ["(", "{", "["]
    for prt in lst:
        if prt in inp:
            stack.append(prt)
        else:
            if stack:
                ele = stack.pop()
                if map[ele] == prt:
                    continue
                else:
                    stack.append(ele)
                    stack.append(prt)
            else:
                stack.append(prt)
    return stack == []
    
        
if __name__ == "__main__":
    
    parent = "{[()([()()]{})]}"
    print(isValid(parent))
    