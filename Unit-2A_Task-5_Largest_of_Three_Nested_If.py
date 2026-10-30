#finding the largest of three numbers 
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("Enter the third number:"))
if a>b:
    largest = a
else:
        largest = b
if b>c:  
        largest = b  
else:
        largest = c  

print(f"Largest = {largest} (among {a}, {b}, {c})")