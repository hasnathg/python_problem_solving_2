# 1. Integer Examples
# Example 1: Temperature Checker

# Check if temperatures are below freezing
temperatures = [4, -2, 5, -5, 0, 3, -1, -3]
negative_count = 0

for temp in temperatures:
    if temp < 0:
        print(f"{temp}°C: Freezing!")
        negative_count += 1
    elif temp == 0:
        print("0°C: Ice point!")
    else:
        print(f"{temp}°C: Above freezing")

print(f"Total freezing days: {negative_count}")


# Example 2: Multiplication Table

# Generate multiplication table for a number
number = 7
counter = 1

while counter <= 10:
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1
else:
    print("Multiplication table complete!")