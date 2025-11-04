# Example 1: Inventory System
# Track and update product inventory

inventory = {"A001": 10, "B205": 5, "C077": 20}
sales = [("A001", 3), ("B205", 4), ("A001", 2)]

for item, qty in sales:
    if qty <= inventory.get(item, 0):
        inventory[item] -= qty
        print(f"Sold {qty} of {item}")
    else:
        print(f"Not enough {item} in stock")

print("\nRemaining inventory:")
for item, stock in inventory.items():
    print(f"{item}: {stock}")


# Example 2: Word Frequency Counter
# Count word frequencies in text
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")