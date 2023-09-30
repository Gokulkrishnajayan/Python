num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==num:
   print("The number "+str(num)+" is an Armstrong number")
else:
   print("The number "+str(num)+" is not an Armstrong number")
