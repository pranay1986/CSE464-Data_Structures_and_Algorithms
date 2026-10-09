"""CSE464 | Circular Singly Linked List.
Algorithm: Keep tail whose next points at head.
Logic: O(1) end insert and front delete.
"""

class Node:
    def __init__(self,x):self.x=x;self.next=None
class CircularList:
    def __init__(self):self.tail=None
    def append(self,x):
        n=Node(x)
        if self.tail:n.next=self.tail.next;self.tail.next=n
        else:n.next=n
        self.tail=n
    def pop_front(self):
        if not self.tail:raise IndexError('empty')
        h=self.tail.next;x=h.x
        if h is self.tail:self.tail=None
        else:self.tail.next=h.next
        return x
    def values(self):
        if not self.tail:return []
        ans=[];p=self.tail.next
        while True:
            ans.append(p.x);p=p.next
            if p is self.tail.next:break
        return ans

if __name__ == "__main__":
    c=CircularList();[c.append(x) for x in (1,2,3)];print(c.pop_front(),c.values())
