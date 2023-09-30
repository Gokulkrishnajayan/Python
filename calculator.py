num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operation=input("Enter the preffered calculation +,-.*,/ : ")
if operation == '+':
   print("{} + {} = {}".format(num1, num2,num1+num2))
elif operation == '-':
   print("{} - {} = {}".format(num1, num2,num1-num2))
elif operation == '*':
   print("{} * {} = {}".format(num1, num2,num1*num2)) 
elif operation == '/':
   print("{} / {} = {}".format(num1, num2,num1/num2))   
else: 
   print("Invalid operation")
