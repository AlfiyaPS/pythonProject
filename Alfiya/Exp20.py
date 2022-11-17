n=int(input("enter the limit"))
n1=0
n2=1
count=0
if(n<=0):
    print("enter a positive number")
else:
    print("fibonacci sequence of the no is")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1