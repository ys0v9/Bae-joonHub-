word=input()
cnt = 0
mo = "aeiou"
for i in word:
    if i in mo:
        cnt+=1

print(cnt)