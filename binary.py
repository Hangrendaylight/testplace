list=list(range(1,101))
def BinarySearch(list,target):
    Low=list[0]
    high=list[-1]
    counter=0
    while True:
        mid=(high+Low)//2
        if mid==target:
            counter+=1
            break
        elif mid>target:
            high=mid-1
            counter+=1
            print(f"counter {counter}: guessed {mid}")
        else:
            Low=mid+1
            counter+=1
            print(f"counter {counter}: guessed {mid}")
    print(f"the number is {mid} with {counter} counts")
while True:
    number=int(input("pick a number: "))
    if 0<=number<=100:
        BinarySearch(list,number)
        break
    else:
        print("please input from 0 to 100")