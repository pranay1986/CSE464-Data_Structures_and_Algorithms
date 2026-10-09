"""CSE464 | Linked Queue.
Algorithm: Keep front and rear pointers to linked nodes.
Logic: Enqueue and dequeue in O(1).
"""

class Node:
    def __init__(self,x):self.x=x;self.next=None
class Queue:
    def __init__(self):self.front=self.rear=None
    def enqueue(self,x):
        n=Node(x)
        if self.rear:self.rear.next=n
        else:self.front=n
        self.rear=n
    def dequeue(self):
        if self.front is None:raise IndexError('underflow')
        x=self.front.x;self.front=self.front.next
        if self.front is None:self.rear=None
        return x

if __name__ == "__main__":
    q=Queue();q.enqueue(8);q.enqueue(9);print(q.dequeue(),q.dequeue())
