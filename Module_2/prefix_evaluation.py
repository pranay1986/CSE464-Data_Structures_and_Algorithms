"""CSE464 | Prefix Evaluation.
Algorithm: Scan prefix tokens in reverse with an operand stack.
Logic: Space-separated numeric tokens.
"""

def evaluate(expr):
    s=[]
    for x in reversed(expr.split()):
        if x not in ('+','-','*','/','^'):s.append(float(x));continue
        a=s.pop();b=s.pop();s.append({'+':lambda:a+b,'-':lambda:a-b,'*':lambda:a*b,'/':lambda:a/b,'^':lambda:a**b}[x]())
    if len(s)!=1:raise ValueError('invalid expression')
    return s[0]

if __name__ == "__main__":
    print(evaluate('+ 2 * 3 4'))
