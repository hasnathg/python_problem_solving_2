# Example 1: Shopping Cart

# Process shopping cart with discounts
cart = [("Apple", 1.2, 3), ("Milk", 2.5, 1), ("Bread", 1.8, 2)]
total = 0.0
discount_threshold = 10

print("Receipt:")
for item in cart:
    name, price, quantity = item
    subtotal = price * quantity
    total += subtotal
    print(f"- {name} x{quantity}: ${subtotal:.2f}")

if total > discount_threshold:
    discount = total * 0.1
    total -= discount
    print(f"Discount applied: -${discount:.2f}")

print(f"Total due: ${total:.2f}")


# Example 2: Prime Number Finder

# Find prime numbers in a range
n = 30
primes = []
candidate = 2

while candidate <= n:
    is_prime = True
    for divisor in primes:
        if divisor * divisor > candidate:
            break
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1

print(f"Primes up to {n}:")
print(primes)


