"""CSE464 | Balanced Brackets.
Algorithm: Match closing symbols against latest unmatched opener.
Logic: Stack-based scan.
"""

def balanced(s):
    match={')':'(',']':'[','}':'{'};stack=[]
    for c in s:
        if c in '([{':stack.append(c)
        elif c in match:
            if not stack or stack.pop()!=match[c]:return False
    return not stack

if __name__ == "__main__":
    print(balanced('{[()]}'),balanced('([)]'))
