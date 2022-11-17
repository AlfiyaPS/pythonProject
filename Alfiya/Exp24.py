str=input("enter the string")
print(str)
dict={}
word=str.split()
for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("word frequency is")
for m,n in dict.items():
    print(m,n)


