import itertools

colors = set()
for _ in range(2):
    colors.update(input().split())

sorted_colors = sorted(colors)

for body, tail in itertools.product(sorted_colors, repeat=2):
    print(body, tail)