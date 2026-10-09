"""CSE464 | Merge Sort.
Algorithm: Sort using merge sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    if len(a)<2:return a[:]
    mid=len(a)//2;l=sort(a[:mid]);r=sort(a[mid:]);out=[];i=j=0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:out.append(l[i]);i+=1
        else:out.append(r[j]);j+=1
    return out+l[i:]+r[j:]

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
