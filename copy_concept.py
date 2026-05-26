# Shallow copy and Deep copy
import copy

original = [[1, 2, 3], [4, 5, 6]]

# 1. Shallow Copy
shallow = copy.copy(original)

# Changing a nested element affects BOTH
shallow[0][0] = 'X'

print("Original after shallow copy change:")
print(original)

print("\nShallow copy")
print(shallow)
# 2. Deep Copy
deep = copy.deepcopy(original)

# Changing a nested element affects ONLY deep copy
deep[1][0] = 'Z'

print("\nOriginal after deep copy change:")
print(original)

print("\nDeep copy:")
print(deep)