"""CSE464 | Priority Queue.
Algorithm: Store priority-labelled items in a binary min-heap.
Logic: Lower numeric priority is served first; sequence breaks ties.
"""

import heapq
class PriorityQueue:
    def __init__(self):self.heap=[];self.seq=0
    def enqueue(self,p,x):heapq.heappush(self.heap,(p,self.seq,x));self.seq+=1
    def dequeue(self):
        if not self.heap:raise IndexError('empty')
        return heapq.heappop(self.heap)[2]

if __name__ == "__main__":
    q=PriorityQueue();q.enqueue(3,'low');q.enqueue(1,'high');q.enqueue(1,'high2');print([q.dequeue() for _ in range(3)])
