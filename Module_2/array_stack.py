"""CSE464 | Array Stack.
Algorithm: Fixed-capacity LIFO ADT.
Logic: top is an integer and overflow/underflow are explicit.
"""

class Stack:
    def __init__(self,capacity):self.a=[None]*capacity;self.top=-1
    def push(self,x):
        if self.top+1==len(self.a):raise OverflowError('full')
        self.top+=1;self.a[self.top]=x
    def pop(self):
        if self.top<0:raise IndexError('empty')
        x=self.a[self.top];self.a[self.top]=None;self.top-=1;return x
    def peek(self):
        if self.top<0:raise IndexError('empty')
        return self.a[self.top]

if __name__ == "__main__":
    s=Stack(2);s.push(10);s.push(20);print(s.pop(),s.peek())
