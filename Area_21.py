

coordinates = list(
    map(lambda s: tuple(map(int, s.split(","))), input().split()))

max_x = max(map(lambda t: t[0], coordinates))
min_x = min(map(lambda t: t[0], coordinates))

max_y = max(map(lambda t: t[1], coordinates))
min_y = min(map(lambda t: t[1], coordinates))

area = abs(max_x-min_x) * abs(max_y-min_y)

print(area)
