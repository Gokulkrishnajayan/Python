def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
operation=input("enter the operations (+,-,*,/,):")

if operation=='+': 
    print("sum of",a,"and ",b,"is",add(a,b))    
elif operation=='-': 
    print("substracting ",a,"from",b,"is",sub(a,b))
elif operation=='*':
    print("multipliying ",a,"and",b,"is",mult(a,b))
elif operation=='/':
    print(a,"divided by ",b,"is",div(a,b))
else:
    print("invalid operator")                
           
            
