number=100
sum=number*(number+1)//2
square_num=sum**2
print(square_num)
number_square=0
index=1
while index<number:
    number_square+=index**2
    index+=1
print(number_square)  
print("the diff is",square_num-number_square)  


