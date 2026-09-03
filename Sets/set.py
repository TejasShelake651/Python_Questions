# Set
numbers = {10, 20, 30, 40, 50}

# 1. add()
numbers.add(60)
print("1.", numbers)

# 2. remove()
numbers.remove(10)
print("2.", numbers)

# 3. discard()
numbers.discard(20)
print("3.", numbers)

# 4. pop()
numbers.pop()
print("4.", numbers)

# 5. copy()
new_set = numbers.copy()
print("5.", new_set)

# 6. union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("6.", set1.union(set2))

# 7. intersection()
print("7.", set1.intersection(set2))

# 8. difference()
print("8.", set1.difference(set2))

# 9. update()
set1.update({6, 7})
print("9.", set1)

# 10. clear()
set3 = {100, 200, 300}
set3.clear()
print("10.", set3)