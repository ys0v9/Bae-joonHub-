answers = [
    [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13],
    [1, 3, 5, 6, 7, 8, 9, 12, 13],
    [1, 3, 5, 6, 7, 8, 9, 12, 13],
    [1, 2, 3, 5, 6, 7, 8, 12, 13],
    [1, 3, 5, 6, 7, 8, 12, 13],
    [1, 3, 5, 6, 7, 8, 12, 13],
    [1, 3, 5, 6, 7, 8, 12, 13],
    [1, 3, 5, 6, 7, 8, 12, 13],
    [1, 3, 5, 6, 7, 8, 12, 13],
    [1, 2, 3, 6, 7, 8, 12, 13]
]

n = int(input())

selected = answers[n - 1]

print(len(selected))

result = []
for i in range(len(selected)):
    num = selected[i]
    letter = chr(num + 64)
    result.append(letter)

print(" ".join(result))
