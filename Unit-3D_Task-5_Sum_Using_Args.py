
def total(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = total(10, 20, 30, 40)
print("Sum =", result)
