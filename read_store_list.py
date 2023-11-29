file_path = 'gokul.txt'
with open(file_path, 'r') as file:
     file_content_list = file.readlines()
print("Content of",file_path,"stored in a list:\n")
for line in file_content_list:
    print(line.strip())
