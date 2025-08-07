def count_369(n):
    cnt = 0
    for i in range(1, n + 1):
        x = i
        while x > 0:
            if x % 10 in [3, 6, 9]:
                cnt += 1
            x //= 10
    return cnt

n = int(input())
print(count_369(n))