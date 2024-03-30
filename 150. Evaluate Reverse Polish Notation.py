class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        operators = {"+", "-", "*", "/"}
        for ele in tokens:

            if ele in operators:
                y =  stack.pop() 
                x =  stack.pop()
                eval_str = x + ele + y
                z = int(eval(eval_str))
                stack.append(str(z))

            else:
                stack.append(ele)
        
        
        return int(stack.pop())
    


