#checking if a person is eligible to voting 
Age=int(input("ENTER THE PERSON AGE:"))
if Age>=18:
    print(f"AGE={Age} ELIGIBLE TO VOTE")
else:
    print(f"AGE={Age} NOT ELIGIBLE TO VOTE")