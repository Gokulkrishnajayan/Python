n = 5
file=open('gokul.txt', 'r')
print("First",n,"lines of",file_path,":\n")
for line in range(n):
    print(file.readline().strip())
