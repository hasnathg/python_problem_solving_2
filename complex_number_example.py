# Example 1: Complex Plane Checker

# Identify quadrant of complex numbers
numbers = [3+4j, -2+3j, -1-1j, 2-3j]

for num in numbers:
    real = num.real
    imag = num.imag
    print(f"Number: {num}")
    
    if real > 0 and imag > 0:
        print("Quadrant I")
    elif real < 0 and imag > 0:
        print("Quadrant II")
    elif real < 0 and imag < 0:
        print("Quadrant III")
    else:
        print("Quadrant IV")


# Example 2: Complex Magnitudes

# Find complex numbers with magnitude > 5
values = [3+2j, 6+8j, 1+1j, 4+3j, 5+0j]
threshold = 5
count = 0

for val in values:
    magnitude = (val.real**2 + val.imag**2)**0.5
    if magnitude > threshold:
        count += 1
        print(f"{val} has magnitude {magnitude:.2f} (>5)")

print(f"{count} numbers exceed magnitude 5")