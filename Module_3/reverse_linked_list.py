"""CSE464 | Reverse Linked List.
Algorithm: Reverse next pointers in one pass.
Logic: Use prev, curr, nxt to preserve remaining nodes.
"""

class Node:
    def __init__(self,x,n=None):self.x=x;self.next=n
def reverse(head):
    prev=None;curr=head
    while curr:
        nxt=curr.next;curr.next=prev;prev=curr;curr=nxt
    return prev
def values(h):
    a=[]
    while h:a.append(h.x);h=h.next
    return a

if __name__ == "__main__":
    h=Node(1,Node(2,Node(3)));print(values(reverse(h)))
