"""CSE464 | Hash Linear Probing.
Algorithm: Probe slots sequentially with tombstones.
Logic: Maintain search chains after deletion.
"""

DELETED=object()
class HashTable:
    def __init__(self,n=7):self.a=[None]*n
    def _probe(self,k):
        for i in range(len(self.a)):yield (k+i)%len(self.a)
    def insert(self,k,v):
        first_deleted=None
        for i in self._probe(k):
            slot=self.a[i]
            if slot is DELETED and first_deleted is None:first_deleted=i
            elif slot is None:
                self.a[first_deleted if first_deleted is not None else i]=(k,v);return
            elif slot is not DELETED and slot[0]==k:self.a[i]=(k,v);return
        if first_deleted is not None:self.a[first_deleted]=(k,v);return
        raise OverflowError('table full')
    def search(self,k):
        for i in self._probe(k):
            slot=self.a[i]
            if slot is None:return None
            if slot is not DELETED and slot[0]==k:return slot[1]
        return None
    def delete(self,k):
        for i in self._probe(k):
            slot=self.a[i]
            if slot is None:return False
            if slot is not DELETED and slot[0]==k:self.a[i]=DELETED;return True
        return False

if __name__ == "__main__":
    h=HashTable();h.insert(1,'a');h.insert(8,'b');h.delete(1);print(h.search(8))
