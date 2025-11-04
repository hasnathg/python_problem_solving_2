# Example 1: Grade Calculator

# Calculate student grade average
grades = [89.5, 92.0, 75.5, 81.0, 68.5]
total = 0.0
count = 0

for grade in grades:
    total += grade
    count += 1

average = total / count
print(f"Average grade: {average:.2f}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
else:
    print("Grade: D")


# Example 2: Circle Measurements

# Calculate circle properties
radius = 5.5
PI = 3.14159
step = 0.5

while radius <= 7.0:
    circumference = 2 * PI * radius
    area = PI * radius ** 2
    print(f"Radius: {radius:.1f}cm")
    print(f"Circumference: {circumference:.2f}cm")
    print(f"Area: {area:.2f}cm²\n")
    radius += step