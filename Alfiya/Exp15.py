list1=[1,2,3,4,5]
list2=[6,7,8,9,2]
a=len(list1)
b=len(list2)
if(a==b):
    print("same length")
else:
    print("not same length")
c=sum(list1)
d=sum(list2)
if(c==d):
    print("sum is same")
else:
    print("sum is not same")
print("common elements")
for i in list1:
    for j in list2:
        if (i==j):
            print(i)


