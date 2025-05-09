salary=int(input("Enter The Salary"))
if salary<=400000:
    print("the tax rate::NIL")
elif 400000<salary<=800000:
    print("the tax rate::5%")
elif 800000<salary<=1200000:
    print("the tax rate::10%")   
elif 1200000<salary<=1600000:
    print("the tax rate::15%")   
elif 1600000<salary<=2000000:
    print("the tax rate::20%")   
elif 2000000<salary<=2400000:
    print("the tax rate::25%")     
elif salary>2400000:
    print("the tax rate::30%") 
else:
    print("enter the salary range in between 400000 and 2400000")         