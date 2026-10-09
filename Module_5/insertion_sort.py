"""CSE464 | Insertion Sort.
Algorithm: Sort using insertion sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    a=a[:]
    for i in range(1,len(a)):
        x=a[i];j=i-1
        while j>=0 and a[j]>x:a[j+1]=a[j];j-=1
        a[j+1]=x
    return a

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
