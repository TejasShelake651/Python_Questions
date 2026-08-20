"""
2. Write a program to develope a system that manages the positions of points in a 2D plane. The position of each point is represented as a tuple of two values: (x, y). Write a program that:
● Takes a list of points as input.
● Calculates the distance between two given points.
● Finds the point that is farthest from the origin (0, 0).
Tasks:
● Use tuples to represent the coordinates of each point.
● Implement a function to calculate the Euclidean distance between two points using their tuple representations.
● Implement a function to find the farthest point from the origin.
"""

import math

def get_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def farthest_from_origin(points):
    if not points:
        return None
    origin = (0, 0)
    farthest = points[0]
    max_dist = get_distance(origin, farthest)
    for p in points[1:]:
        dist = get_distance(origin, p)
        if dist > max_dist:
            max_dist = dist
            farthest = p
    return farthest

points = [(1, 2), (3, 4), (-5, -5)]
print("Distance:", get_distance(points[0], points[1]))
print("Farthest from origin:", farthest_from_origin(points))
