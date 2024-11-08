x = 7
y = 1

points = [(x, y)]

while x != y:
    print(x, y)
    x = round(x + 3, 2)
    y = round(y + 3, 2)
    points.append((x, y))
    x = round(x / 2, 2)
    y = round(y / 2, 2)
    points.append((x, y))

print(", ".join([f"({i[0]}, {i[1]})" for i in points]))
