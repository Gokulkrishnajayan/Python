def binary_to_decimal(binary):
    return int(binary, 2)

binary = input("Enter a binary number: ")
decimal= binary_to_decimal(binary)
print("The decimal equivalent of",binary,"is",decimal)


