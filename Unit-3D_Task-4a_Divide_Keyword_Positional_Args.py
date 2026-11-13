def divide(a,b):
    return a/b

a=int(input("Enter the number a:"))
b=int(input("enter the number b:"))
print("divide_formal_parameters=",divide(a,b))

result = divide(b=15,a=30)
print("divide_keyword_args=",result)