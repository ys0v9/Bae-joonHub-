while True:
    code = input()
    if code == "END":
        break
    else:
        for i in range(len(code)-1,-1,-1):
            print(code[i], end='')
        print()