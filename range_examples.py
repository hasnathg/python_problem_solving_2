# Example 1: Stepped Countdown

# Count down with custom steps
start = 20
end = 0
step = -3
current = start

print("Countdown:")
while current > end:
    print(current)
    current += step
else:
    print("Ignition!")


# Example 2: Grid Generator

# Generate grid coordinates
rows = range(1, 4)
cols = range(1, 3)
grid = []

for r in rows:
    for c in cols:
        grid.append((r, c))

print("2x3 Grid Coordinates:")
print(grid)