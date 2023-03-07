def calculate_area(base, height):
    return 0.5 * base * height

b = int(input("Enter base: "))
h = int(input("Enter height: "))
a = calculate_area(b, h)
print("Area of triangle:", a)