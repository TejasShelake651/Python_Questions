# Frozenset
fs1 = frozenset({10, 20, 30, 40})
fs2 = frozenset({30, 40, 50, 60})

# 1. union()
print("1.", fs1.union(fs2))

# 2. intersection()
print("2.", fs1.intersection(fs2))

# 3. difference()
print("3.", fs1.difference(fs2))

# 4. symmetric_difference()
print("4.", fs1.symmetric_difference(fs2))

# 5. issubset()
print("5.", fs1.issubset(fs2))

# 6. issuperset()
print("6.", fs1.issuperset(fs2))

# 7. isdisjoint()
print("7.", fs1.isdisjoint(fs2))

# 8. copy()
print("8.", fs1.copy())

# 9. len()
print("9.", len(fs1))

# 10. max()
print("10.", max(fs1))