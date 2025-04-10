def sortAge(person):
    return person[0]  

n = int(input())  

people = []
for _ in range(n):
    age, name = input().split()
    people.append([int(age), name]) 

people.sort(key=sortAge) 

for person in people:
    print(person[0], person[1])