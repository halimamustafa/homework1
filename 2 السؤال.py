def bincal(dnum):
    binnum=list()
    while dnum!=0:
        i=dnum%2
        dnum//=2
        binnum.append(i)
    binnum.reverse()
    return binnum

dnum=int(input('enter dnum'))
l=bincal(dnum)
for i in l:
    print(i,end="")
