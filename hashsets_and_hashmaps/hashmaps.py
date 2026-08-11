# Hashmaps - Dictionaries

d = {'ag' : 1, 'bob' : 2, 'rob' : 3}

print(d)

# Add key:value pair - O(1)
d['tom'] = 4
print(d)

# Contains - O(1)
if 'ag' in d:
    print("d contains 'ag'")

# Get corresponding value - O(1)
print(d['ag'])

# Loop over key:value pair - O(n)
for key, value in d.items():
    print(f'(key: {key}) : (value : {value})')

# The following are useful for leetcode

# Defaultdict - if a value is not present in the dictionary, it automatically gets the dtype default
# for integers: 0, strings: ''

from collections import defaultdict

default = defaultdict(int)

print(default[2])
print(default)

# Counter - used to count elements easily
# Might be risky to use in a technical interview because it is a python shortcut

from collections import Counter

string = 'aaaaaabbbbbccccddd'
counter = Counter(string)

print(f"Counter Dict: {counter}")

