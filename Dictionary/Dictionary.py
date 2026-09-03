student = {
    "name": "Tejas",
    "age": 21,
    "city": "Pune"
}

# 1. get()
print(student.get("name"))

# 2. keys()
print(student.keys())

# 3. values()
print(student.values())

# 4. items()
print(student.items())

# 5. update()
student.update({"age": 22})
print(student)

# 6. pop()
student.pop("city")
print(student)

# 7. copy()
new = student.copy()
print(new)

# 8. setdefault()
student.setdefault("course", "CSE")
print(student)

# 9. len()
print(len(student))

# 10. clear()
new.clear()
print(new)