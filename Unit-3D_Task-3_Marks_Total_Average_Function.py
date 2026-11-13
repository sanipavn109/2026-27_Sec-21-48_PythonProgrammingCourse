def total_and_average( mark1,mark2,mark3):
    total = mark1+mark2+mark3
    average = mark1+mark2+mark3/3
    return total,average

m1,m2,m3 = 50,89,67
total, average = total_and_average(50,89,67)
print("Total=",total)
print("Average=",average)
