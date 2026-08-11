# Hashsets

s = set()

print(f"s: {s}")

# Add items to hashset - O(1)
s.add(1)
s.add(2)
s.add(3)

print(f"s: {s}")

# Contains - O(1)
if 1 in s:
    print("s contains 1")

# Remove items from hashset - O(1)
s.remove(3)

print(f"s: {s}")

print()

# Construct set of string - O(S); where S is the string length
string = 'aaaaaabbbbbccccddd'
string_set = set(string)

print(f"String: {string}")
print(f"String set: {string_set}")

print()

# Loop over items in set - O(n)
print("Set Items:")
for x in s:
    print(x)
