"""CSE464 | Postfix Evaluation.
Algorithm: Read postfix tokens left-to-right and evaluate from operand stack.
Logic: Space-separated numeric tokens; operator pops right then left.
"""

def evaluate(expr):
    s=[]
    for x in expr.split():
        if x not in ('+','-','*','/','^'):s.append(float(x));continue
        b=s.pop();a=s.pop();s.append({'+':lambda:a+b,'-':lambda:a-b,'*':lambda:a*b,'/':lambda:a/b,'^':lambda:a**b}[x]())
    if len(s)!=1:raise ValueError('invalid expression')
    return s[0]

if __name__ == "__main__":
    print(evaluate('2 3 4 * +'))
