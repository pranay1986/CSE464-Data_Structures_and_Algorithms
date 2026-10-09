"""CSE464 | Middle Of Linked List.
Algorithm: Use slow and fast references.
Logic: Fast advances twice as quickly; second middle is returned for even lengths.
"""

class Node:
    def __init__(self,x,n=None):self.x=x;self.next=n
def middle(head):
    slow=fast=head
    while fast and fast.next:slow=slow.next;fast=fast.next.next
    return slow.x if slow else None

if __name__ == "__main__":
    print(middle(Node(1,Node(2,Node(3,Node(4,Node(5)))))))
