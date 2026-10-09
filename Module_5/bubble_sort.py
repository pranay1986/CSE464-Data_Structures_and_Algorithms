"""CSE464 | Bubble Sort.
Algorithm: Sort using bubble sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    a=a[:]
    for end in range(len(a)-1,0,-1):
        changed=False
        for i in range(end):
            if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i];changed=True
        if not changed:break
    return a

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
