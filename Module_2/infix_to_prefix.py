"""CSE464 | Infix To Prefix.
Algorithm: Reverse the postfix reasoning via recursive parsing of precedence.
Logic: Single-letter operands and parentheses, exponent is right-associative.
"""

def prefix(expr):
    s=expr.replace(' ','');i=0
    def parse(minprec=0):
        nonlocal i
        if i>=len(s):raise ValueError('missing operand')
        if s[i]=='(':
            i+=1;left=parse()
            if i>=len(s) or s[i]!=')':raise ValueError('mismatched')
            i+=1
        else:
            left=s[i];i+=1
            if not left.isalnum():raise ValueError('invalid operand')
        prec={'+':1,'-':1,'*':2,'/':2,'^':3}
        while i<len(s) and s[i] in prec and prec[s[i]]>=minprec:
            op=s[i];i+=1;right=parse(prec[op]+(0 if op=='^' else 1));left=op+' '+left+' '+right
        return left
    result=parse()
    if i!=len(s):raise ValueError('invalid expression')
    return result

if __name__ == "__main__":
    print(prefix('A*(B+C)'))
