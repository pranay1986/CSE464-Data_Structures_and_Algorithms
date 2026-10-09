"""CSE464 | Circular Queue.
Algorithm: Wrap indices modulo capacity to reuse array slots.
Logic: Track size to distinguish empty/full.
"""

class CircularQueue:
    def __init__(self,n):
        if n<=0:raise ValueError('capacity must be positive')
        self.a=[None]*n;self.front=0;self.count=0
    def enqueue(self,x):
        if self.count==len(self.a):raise OverflowError('full')
        self.a[(self.front+self.count)%len(self.a)]=x;self.count+=1
    def dequeue(self):
        if not self.count:raise IndexError('empty')
        x=self.a[self.front];self.a[self.front]=None;self.front=(self.front+1)%len(self.a);self.count-=1;return x

if __name__ == "__main__":
    q=CircularQueue(2);q.enqueue(1);q.enqueue(2);print(q.dequeue());q.enqueue(3);print(q.dequeue(),q.dequeue())
