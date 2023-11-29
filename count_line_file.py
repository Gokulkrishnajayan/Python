file_path = 'gokul.txt'
with open(file_path, 'r') as file:
     file_content_list = file.readlines()
print("Number of line in the file:",len(file_content_list))


