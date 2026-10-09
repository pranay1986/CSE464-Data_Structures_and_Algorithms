"""CSE464 | Array Operations.
Algorithm: Traverse, insert at an index by right-shifting, delete by left-shifting.
Logic: Explicit shifts illustrate classical array costs.
"""

def insert(a,n,x,i):
    if not 0<=i<=n<len(a): raise IndexError('invalid position or full array')
    for k in range(n,i,-1): a[k]=a[k-1]
    a[i]=x
    return n+1

def delete(a,n,i):
    if not 0<=i<n: raise IndexError(i)
    x=a[i]
    for k in range(i,n-1): a[k]=a[k+1]
    a[n-1]=None
    return n-1,x

if __name__ == "__main__":
    a=[10,20,30,None,None];n=3;n=insert(a,n,15,1);print(a[:n]);n,x=delete(a,n,2);print(x,a[:n])
