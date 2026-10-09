"""CSE464 | Loop Growth Counts.
Algorithm: Instrument representative linear, logarithmic, triangular loops.
Logic: Count operations without relying on wall-clock time.
"""

def counts(n):
    linear=sum(1 for _ in range(n))
    logarithmic=0;i=1
    while i<=n:logarithmic+=1;i*=2
    triangular=sum(1 for i in range(1,n+1) for _ in range(i))
    return linear,logarithmic,triangular

if __name__ == "__main__":
    print(counts(8))
