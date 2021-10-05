struct="Halmlabimmbam"

operand = "m"

start = 4

i = 11

positions = [pos for pos, char in enumerate(struct[start-1:i+1]) if char == operand]

print(positions)