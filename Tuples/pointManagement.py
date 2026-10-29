# Point Management System (Tuple coordinates & Euclidean distance)

def distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return (x * x + y * y) ** 0.5

def farthest_point(points):
    if not points:
        return None
    farthest = points[0]
    max_dist = (points[0][0]**2 + points[0][1]**2) ** 0.5
    for p in points:
        dist = (p[0]**2 + p[1]**2) ** 0.5
        if dist > max_dist:
            max_dist = dist
            farthest = p
    return farthest

if __name__ == "__main__":
    points = [(1, 2), (4, 6), (9, 12), (0, 0)]
    print("Points:", points)
    print("Distance between first two points:", distance(points[0], points[1]))
    print("Farthest point from origin:", farthest_point(points))
