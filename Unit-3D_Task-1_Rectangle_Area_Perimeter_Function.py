def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

a, p = rectangle(l, b)

print("Area of rectangle =", a)
print("Perimeter of rectangle =", p)