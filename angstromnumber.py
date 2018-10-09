x=int(input("enter any number"))
s=0
z=x
while x>0:
 y=x%10
 s=y**3+5
s=x//10
print(s)
if s==z:
 print("angstrom number")
else:
 print("not an angstrom number")
