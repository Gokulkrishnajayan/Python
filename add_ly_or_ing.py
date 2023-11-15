a=input("Enter a string")
if a.endswith("ing"):
    a=a+("ly") 
elif a.endswith("ly"):
    a=a+("ing") 
print(a)     
    
