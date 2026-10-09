"""CSE464 | Linear Queue.
Algorithm: Array FIFO with front and rear indices.
Logic: Show false overflow after removals.
"""

class Queue:
    def __init__(self,n):self.a=[None]*n;self.front=0;self.rear=-1
    def enqueue(self,x):
        if self.rear+1==len(self.a):raise OverflowError('rear exhausted')
        self.rear+=1;self.a[self.rear]=x
    def dequeue(self):
        if self.front>self.rear:raise IndexError('empty')
        x=self.a[self.front];self.front+=1;return x

if __name__ == "__main__":
    q=Queue(3);q.enqueue(5);q.enqueue(6);print(q.dequeue(),q.dequeue())
