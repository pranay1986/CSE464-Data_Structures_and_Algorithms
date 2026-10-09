"""CSE464 | Linked Stack.
Algorithm: Use list head as stack top.
Logic: Push/pop in O(1).
"""

class Node:
    def __init__(self,x,n=None):self.x=x;self.next=n
class Stack:
    def __init__(self):self.head=None
    def push(self,x):self.head=Node(x,self.head)
    def pop(self):
        if self.head is None:raise IndexError('underflow')
        x=self.head.x;self.head=self.head.next;return x

if __name__ == "__main__":
    s=Stack();s.push(1);s.push(2);print(s.pop(),s.pop())
