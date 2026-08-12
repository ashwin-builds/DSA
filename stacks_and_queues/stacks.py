# Stacks - implemented using a dynamic array
# LIFO - last in, first out

stack = []
print(f"Stack: {stack}")

# Append to top of stack - O(1)*
stack.append(1)
stack.append(2)
stack.append(3)

print(f"Stack: {stack}")

# Pop from top of stack - O(1)
x = stack.pop()
print(f"Removed Element: {x}")

print(f'Stack: {stack}')

# Peak - O(1)
print(f"Top of stack element: {stack[-1]}")

# is_empty - O(1)
if stack:
    print(True)
else:
    print(False)
