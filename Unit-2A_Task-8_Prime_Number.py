#checking whether the given number is prime or not
n = int(input("Enter a number (1-100): "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")  
    else:
        print("Prime")