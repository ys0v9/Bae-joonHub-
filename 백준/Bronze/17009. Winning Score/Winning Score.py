apple = 0
banana = 0

for i in range(3, 0, -1):
  apple += i * int(input())

for i in range(3, 0, -1):
  banana += i * int(input())

if apple > banana:
    print('A')
elif apple < banana:
    print('B')
else:
  print('T')