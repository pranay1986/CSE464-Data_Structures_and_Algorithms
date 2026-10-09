"""CSE464 | Delete Given Node.
Algorithm: Copy successor payload and bypass successor.
Logic: Only works for non-tail singly linked nodes.
"""

class Node:
    def __init__(self,x,n=None):self.x=x;self.next=n
def delete_given(node):
    if node is None or node.next is None:raise ValueError('cannot delete tail')
    node.x=node.next.x;node.next=node.next.next

if __name__ == "__main__":
    h=Node(1,Node(2,Node(3)));delete_given(h.next);print([h.x,h.next.x])
