num=int(input("Enter the number:"))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")
