lb=int(input("Enter the lower bound"))
ub=int(input("Enter the upper bound"))
for i in range(lb,ub+1):
    if i>1:
        for j in range (2,i):  
            if (i % j) == 0:  
                break 
        else:    
            print(i)  
