num=int(input("Enter the number: "))
flag=0
if num==1:
    print(num,"is not a prime number")
elif num>1:    
    for i in range(1,num):
        if num%i==0:
           flag=1
           break
if flag==1:
    print(num,"is a prime number")
else:
    print(num,"not a prime number")
        
