#name= akash santosh more
# roll no.=41   #Gr No.=11810832
#div=M    batch=M2

num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10

if num==sum:
        print(num,"is an Armstrong number")
else:
        print(num,"is not an Armstrong number")
        
