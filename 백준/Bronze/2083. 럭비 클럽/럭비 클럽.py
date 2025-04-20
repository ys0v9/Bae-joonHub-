while True:
    name, age, w = input().split()
    age = int(age)
    w = int(w)
    if name == '#' and age == 0 and w == 0:
        break
    else:
        if age>=18 or w >=80:
            member = "Senior"
        else:
            member = "Junior"
    print(name,member)