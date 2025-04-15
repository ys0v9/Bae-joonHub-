while True:
    line = input()
    if line == '#':
        break
    count = 0
    for ch in line.lower():
        if ch in 'aeiou':
            count += 1
    print(count)