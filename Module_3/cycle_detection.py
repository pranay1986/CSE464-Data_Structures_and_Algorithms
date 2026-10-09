"""CSE464 | Cycle Detection.
Algorithm: Floyd tortoise/hare test.
Logic: If fast catches slow, the list contains a cycle.
"""

class Node:
    def __init__(self,x):self.x=x;self.next=None
def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next;fast=fast.next.next
        if slow is fast:return True
    return False

if __name__ == "__main__":
    a,b,c=Node(1),Node(2),Node(3);a.next=b;b.next=c;c.next=b;print(has_cycle(a));c.next=None;print(has_cycle(a))
