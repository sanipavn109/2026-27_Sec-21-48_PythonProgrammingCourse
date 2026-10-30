#finding the smallest of three numbers 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a<b:
    smallest = a
else :
       smallest = b
if b<c:
     smallest = b
else :
       smallest = c
print(f"smallest = {smallest} among {a},{b},{c}")