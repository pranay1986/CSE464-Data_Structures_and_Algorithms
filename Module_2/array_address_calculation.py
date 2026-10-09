"""CSE464 | Array Address Calculation.
Algorithm: Compute offsets in row- and column-major order.
Logic: Apply lower bounds and element width.
"""

def address_2d(base,width,rows,cols,i,j,lr=0,lc=0,order='row'):
    if not(lr<=i<lr+rows and lc<=j<lc+cols):raise IndexError()
    offset=(i-lr)*cols+(j-lc) if order=='row' else (j-lc)*rows+(i-lr)
    return base+width*offset

if __name__ == "__main__":
    print(address_2d(1000,4,5,6,4,5,1,1))
