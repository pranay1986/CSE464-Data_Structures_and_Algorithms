"""CSE464 | Hash Chaining.
Algorithm: Map keys to buckets and handle collisions with lists.
Logic: Hash index key mod capacity; unique keys.
"""

class HashTable:
    def __init__(self,n=7):self.a=[[] for _ in range(n)]
    def insert(self,k,v):
        b=self.a[k%len(self.a)]
        for pair in b:
            if pair[0]==k:pair[1]=v;return
        b.append([k,v])
    def search(self,k):
        for key,val in self.a[k%len(self.a)]:
            if key==k:return val
        return None
    def delete(self,k):
        b=self.a[k%len(self.a)]
        for i,(key,val) in enumerate(b):
            if key==k:b.pop(i);return True
        return False

if __name__ == "__main__":
    h=HashTable();h.insert(1,'a');h.insert(8,'b');print(h.search(8),h.delete(1),h.search(1))
