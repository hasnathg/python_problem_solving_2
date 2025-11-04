# Example 1: Username Validator

# Validate username requirements
username = "Python_User_123"
has_upper = False
has_digit = False

for char in username:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True

if len(username) >= 8:
    if has_upper and has_digit:
        print("Valid username!")
    else:
        print("Invalid: Needs uppercase letter and number")
else:
    print("Invalid: Too short (min 8 characters)")

# Example 2: Secret Decoder

# Decode message by shifting characters
encoded = "Ifmmp!xpsme"
decoded = ""
shift = 1

for char in encoded:
    if char.isalpha():
        new_char = chr(ord(char) - shift)
        decoded += new_char
    else:
        decoded += char

print(f"Original: {encoded}")
print(f"Decoded: {decoded}")