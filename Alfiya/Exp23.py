a=input("enter the string")
print(a)
dict={ }
for i in a:
    if i in dict:
        dict[i]+=1
        print(dict)
    else:
        dict[i]=1
        print(dict)
print("character frequency is")
for k,v in dict.items():
    print(k,v)