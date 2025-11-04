# Example 1: Network Packet Check

# Validate packet start/end markers
packet = b'\x02Hello\x03'
valid_start = False
valid_end = False

if packet[0] == 0x02:
    valid_start = True
if packet[-1] == 0x03:
    valid_end = True

print(f"Packet: {packet}")
if valid_start and valid_end:
    content = packet[1:-1].decode('utf-8')
    print(f"Valid packet! Content: '{content}'")
else:
    print("Invalid packet markers")


# Example 2: ASCII Art Generator

# Create byte-based ASCII art
byte_values = [66, 65, 83, 73, 67]  # 'BASIC' in ASCII
art = b''
row = 1

while row <= 5:
    for byte_val in byte_values:
        char = bytes([byte_val])
        art += char * row + b' '
    art += b'\n'
    row += 1

print("ASCII Art:")
print(art.decode('utf-8'))