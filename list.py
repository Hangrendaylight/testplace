drinks=['coffee','tea','coconut','smoothie']
prices=[25000,20000,30000,15000,10000]
def linearSearch(drinks,target):
    for i in range(len(drinks)):
        if drinks[i]==target:
            return i
        else:
            return -1
while True:
    a=input("input your drink: ")
    pos=linearSearch(drinks,a)
    if pos!=-1:
        print(drinks[pos])
        print("price:",prices[pos],"VND")
        break
    else:
        print("drink not found")

