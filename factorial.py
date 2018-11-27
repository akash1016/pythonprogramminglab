#name=akash more
#roll no =41 Gr no=1810832
#div=M batch=M2


def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
x=int(input("enter x : "))
y=fact(x)
print ("{}!= {}".format(x,y))
    
