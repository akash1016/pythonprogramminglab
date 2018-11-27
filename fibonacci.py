#name=akash more 
#roll mo=41 gr no=11810832
#div=M batch=M2

n=int(input("enter a number:"))
a=0
b=1
l=[]
if n<0:
    print("enter a positive number")
elif n==0:
    print("0")
elif n==1:
    print("0,1")
else:
    l.append(a)
    l.append(b)
for i in range(n-2):
    f=a+b
    l.append(f)
    a=b
    b=f
print(l)
    
