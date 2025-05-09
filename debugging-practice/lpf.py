n=int(input("enter the number"))
index=n-1
while index>1:
    if n%index==0:
        print(index)
    index=index-1
