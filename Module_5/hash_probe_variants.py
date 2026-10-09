"""CSE464 | Hash Probe Variants.
Algorithm: Compare linear, quadratic, double-hash probe sequences.
Logic: Prime table size; double-hash step 1+key mod (m-1).
"""

def probes(k,m,mode):
    if m<3:raise ValueError('m >= 3')
    h=k%m;step=1+(k%(m-1))
    for i in range(m):
        if mode=='linear':yield (h+i)%m
        elif mode=='quadratic':yield (h+i*i)%m
        elif mode=='double':yield (h+i*step)%m
        else:raise ValueError(mode)

if __name__ == "__main__":
    for mode in ('linear','quadratic','double'):print(mode,list(probes(15,11,mode))[:4])
