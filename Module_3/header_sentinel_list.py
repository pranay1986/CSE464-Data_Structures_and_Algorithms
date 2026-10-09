"""CSE464 | Header Sentinel List.
Algorithm: Maintain a dummy head to simplify edge cases.
Logic: Insert/delete uniformly via predecessor.
"""

class Node:
    def __init__(self,x=None,n=None):self.x=x;self.next=n
class HeaderList:
    def __init__(self):self.header=Node()
    def prepend(self,x):self.header.next=Node(x,self.header.next)
    def delete(self,x):
        p=self.header
        while p.next and p.next.x!=x:p=p.next
        if p.next:p.next=p.next.next;return True
        return False
    def values(self):
        a=[];p=self.header.next
        while p:a.append(p.x);p=p.next
        return a

if __name__ == "__main__":
    h=HeaderList();h.prepend(2);h.prepend(1);print(h.delete(2),h.values())
