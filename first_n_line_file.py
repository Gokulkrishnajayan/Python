file_path = 'gokul.txt'
n = 5
file=open(file_path, 'r')
print("First",n,"lines of",file_path,":\n")
for line in range(n):
    print(file.readline().strip())
