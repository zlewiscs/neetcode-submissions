class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_set = {'+', '-', '*', '/'}
        
        stack = deque()

        for token in tokens:
            if token not in op_set:
                stack.append(int(token))
            else:
                tok1 = int(stack.pop())
                tok2 = int(stack.pop())

                if (token == '+'):
                    stack.append(tok1 + tok2)
                elif (token == '-'):
                    stack.append(tok2 - tok1)
                elif (token == '*'):
                    stack.append(tok1 * tok2)
                else:
                    stack.append(int(float(tok2) / tok1))
        
        return stack.pop()