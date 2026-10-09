"""CSE464 | Singly Linked List.
Algorithm: Maintain linked nodes with head reference.
Logic: Implement insertion, removal and traversal.
"""

class Node:
    def __init__(self,x,next=None):self.data=x;self.next=next
class SinglyList:
    def __init__(self):self.head=None
    def append(self,x):
        if not self.head:self.head=Node(x);return
        p=self.head
        while p.next:p=p.next
        p.next=Node(x)
    def prepend(self,x):self.head=Node(x,self.head)
    def search(self,x):
        p=self.head;i=0
        while p:
            if p.data==x:return i
            p=p.next;i+=1
        return -1
    def delete(self,x):
        dummy=Node(None,self.head);p=dummy
        while p.next and p.next.data!=x:p=p.next
        if p.next:p.next=p.next.next
        self.head=dummy.next
    def values(self):
        result=[];p=self.head
        while p:result.append(p.data);p=p.next
        return result

if __name__ == "__main__":
    a=SinglyList();[a.append(x) for x in (10,20,30)];a.prepend(5);a.delete(20);print(a.values(),a.search(30))
