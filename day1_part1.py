def Decode(codes):
    cur = 50
    ans = 0
    for i in codes:
        if not i:
            continue
        if i[0] == 'L':
            temp = int(i[1:])
            cur -= temp
            while cur<0:
                cur += 100
        elif i[0] == 'R':
            temp = int(i[1:])
            cur += temp
            while cur>=100:
                cur -= 100
        if cur == 0:
            ans+=1

    return ans

inp = []
for i in range(4269):                                       # My Puzzle Input size: 4269 
    temp = input()
    inp.append(temp)

print(f"ans: {Decode(inp)}")
        