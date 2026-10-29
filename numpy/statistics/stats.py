import numpy as np

# Statistical and Aggregation Operations in NumPy

nums = np.array([10, 20, 30, 40, 50])
print("Array:", nums)

print("Sum:", np.sum(nums))
print("Average (Mean):", np.mean(nums))
print("Standard Deviation:", np.std(nums))
print("Maximum Value:", np.max(nums))
print("Minimum Value:", np.min(nums))
print("Index of Maximum Value (argmax):", np.argmax(nums))
print("Index of Minimum Value (argmin):", np.argmin(nums))
