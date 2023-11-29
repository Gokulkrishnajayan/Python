file_path = 'gokul.txt'

with open(file_path, 'r') as file:
    print("Initial content of", file_path, ":")
    print(file.read())

with open(file_path, 'a') as file:
    text_to_append = "appending new lines"
    file.write(text_to_append)
    
with open(file_path, 'r') as file:
    updated_content = file.read()
    print("\nafter appending:")
    print(updated_content)
