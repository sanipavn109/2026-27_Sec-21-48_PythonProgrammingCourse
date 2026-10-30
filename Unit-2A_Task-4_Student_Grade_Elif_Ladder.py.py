#printing the students grade by the marks using elif ladder 
score=int(input("ENTER THE STUDENT SCORE:"))
if score>=90 and score<100:
    print(f"marks={score} GRADE:A")
elif score>=80 and score<90:
    print(f"marks={score} GRADE:B")
elif score>=70 and score<80:
    print(f"marks={score} GRADE:C")
else:
    print(f"marks={score} GRADE:D" )