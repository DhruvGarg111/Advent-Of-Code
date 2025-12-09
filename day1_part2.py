def DecodePartTwo(codes):
    cur = 50
    ans = 0
    
    for i in codes:
        dist = int(i[1:])
        
        step = 1 if i[0] == 'R' else -1
        
        for _ in range(dist):
            cur += step
            
            if cur == 100:
                cur = 0
            elif cur == -1:
                cur = 99
            
            if cur == 0:
                ans += 1
                
    return ans

inp = []
for i in range(4269):                           # My Puzzle Input size: 4269 
    temp = input()
    inp.append(temp)

print(f"ans: {DecodePartTwo(inp)}")