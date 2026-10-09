"""CSE464 | Doubly Linked List.
Algorithm: Maintain prev/next links and head/tail.
Logic: O(1) operations at both ends.
"""

class Node:
    def __init__(self,x):self.x=x;self.prev=self.next=None
class DoublyList:
    def __init__(self):self.head=self.tail=None
    def append(self,x):
        n=Node(x);n.prev=self.tail
        if self.tail:self.tail.next=n
        else:self.head=n
        self.tail=n
    def pop_back(self):
        if not self.tail:raise IndexError('empty')
        x=self.tail.x;self.tail=self.tail.prev
        if self.tail:self.tail.next=None
        else:self.head=None
        return x
    def values(self):
        p=self.head;r=[]
        while p:r.append(p.x);p=p.next
        return r

if __name__ == "__main__":
    d=DoublyList();[d.append(x) for x in (5,6,7)];print(d.pop_back(),d.values())
