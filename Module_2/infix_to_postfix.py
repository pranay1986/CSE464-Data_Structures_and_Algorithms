"""CSE464 | Infix To Postfix.
Algorithm: Use operator stack, respecting precedence and right-associative exponentiation.
Logic: Single-letter/digit operands; no unary operators.
"""

def postfix(expr):
    prec={'+':1,'-':1,'*':2,'/':2,'^':3};stack=[];out=[]
    for ch in expr.replace(' ',''):
        if ch.isalnum():out.append(ch)
        elif ch=='(':stack.append(ch)
        elif ch==')':
            while stack and stack[-1]!='(':out.append(stack.pop())
            if not stack:raise ValueError('mismatched parentheses')
            stack.pop()
        elif ch in prec:
            while stack and stack[-1]!='(' and (prec[stack[-1]]>prec[ch] or (prec[stack[-1]]==prec[ch] and ch!='^')):out.append(stack.pop())
            stack.append(ch)
        else:raise ValueError('invalid character')
    while stack:
        x=stack.pop()
        if x=='(':raise ValueError('mismatched parentheses')
        out.append(x)
    return ''.join(out)

if __name__ == "__main__":
    print(postfix('A*(B+C)'))
