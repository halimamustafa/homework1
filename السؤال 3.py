name=input("input yourname")
filename=input("input file name")
infile=open(filename,'r')
outfile=open("1.txt","w")
qq=[line.rstrip().split('=') for line in infile]
infile.close()
print("l=['halima','rama','rima','ola','yara','karam']")
t=0
for q in qq:
    print(q[0])
    a=input()
    if a==q[-1]:
        t+=1
towrite=f"user name: {name} , result {t} , numofquestion: {len(qq)}"
print(towrite)
outfile.write(towrite)
outfile.close()
