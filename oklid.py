points = [(1, 2), (3, 4), (6, 8), (2, 1)]

def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance =euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)


print("Noktalar arasındaki mesafe:", distances)
print("En küçük mesafe:", min_distance)
