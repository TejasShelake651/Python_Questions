# Project Employee Analysis using Set Operations

project1 = {"Amit", "Rahul", "Chetan", "Rohit"}
project2 = {"Chetan", "Rohit", "Sneha", "Priya"}

print("Project 1 Team:", project1)
print("Project 2 Team:", project2)

print("\nEmployees working on both projects (Intersection):", project1.intersection(project2))
print("Employees working only on Project 1 (Difference):", project1.difference(project2))
print("Employees working only on Project 2 (Difference):", project2.difference(project1))
print("Total unique employees across all projects (Union):", project1.union(project2))
print("Employees working on exactly one project (Symmetric Difference):", project1.symmetric_difference(project2))
