def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32

celsius = float(input("Enter the celsius temperature:"))
print("fahrenheit=",celsius_to_fahrenheit(celsius))
