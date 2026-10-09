"""CSE464 | Circular Doubly Linked List.
Algorithm: Keep head and tail with circular bidirectional links.
Logic: Insert and remove at front with constant pointer changes.
"""

class Node:
    def __init__(self,x):self.x=x;self.next=self.prev=self
class CircularDoubly:
    def __init__(self):self.head=None
    def append(self,x):
        n=Node(x)
        if not self.head:self.head=n;return
        tail=self.head.prev;n.prev=tail;n.next=self.head;tail.next=n;self.head.prev=n
    def pop_front(self):
        if not self.head:raise IndexError('empty')
        h=self.head;x=h.x
        if h.next is h:self.head=None
        else:
            tail=h.prev;self.head=h.next;tail.next=self.head;self.head.prev=tail
        return x
    def values(self):
        if not self.head:return []
        p=self.head;a=[]
        while True:
            a.append(p.x);p=p.next
            if p is self.head:return a

if __name__ == "__main__":
    d=CircularDoubly();[d.append(x) for x in (1,2,3)];print(d.pop_front(),d.values())
