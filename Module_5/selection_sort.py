"""CSE464 | Selection Sort.
Algorithm: Sort using selection sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    a=a[:]
    for i in range(len(a)):
        j=min(range(i,len(a)),key=lambda k:a[k]);a[i],a[j]=a[j],a[i]
    return a

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
