s = input()
t = input()

s_len = len(s)
t_len = len(t)

if s_len*t == t_len*s:
    print(1)
else:
    print(0)