"""CSE464 | Expression Tree.
Algorithm: Construct tree from space-separated postfix tokens.
Logic: Operators pop two subtrees; evaluate recursively.
"""

class Node:
    def __init__(self,x,l=None,r=None):self.x=x;self.left=l;self.right=r
def build(postfix):
    s=[]
    for x in postfix.split():
        if x in ('+','-','*','/'):
            r=s.pop();l=s.pop();s.append(Node(x,l,r))
        else:s.append(Node(float(x)))
    if len(s)!=1:raise ValueError('malformed expression')
    return s[0]
def evaluate(n):
    if n.left is None:return n.x
    a=evaluate(n.left);b=evaluate(n.right)
    return {'+':lambda:a+b,'-':lambda:a-b,'*':lambda:a*b,'/':lambda:a/b}[n.x]()

if __name__ == "__main__":
    print(evaluate(build('2 3 4 * +')))
