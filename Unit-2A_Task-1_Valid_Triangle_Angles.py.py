#checking the angles whether they are the valid triangle angles or not 
angle_1=float(input("Enter the angle 1:"))
angle_2=float(input("Enter the angle 2:"))
angle_3=float(input("Enter the angle 3:"))
if angle_1>0 and angle_2>0 and angle_3>0 and angle_1 + angle_2 + angle_3 == 180:
    print(f"valid triangle (angles={angle_1},{angle_2},{angle_3})")
else:
    print(f"not a valid triangle(angles = {angle_1},{angle_2},{angle_3})")