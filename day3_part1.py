def joltage(arr):
    ans = 0
    for s in arr:    
        ans += biggest2(s)
    return ans

def biggest2(num_str):
    best = -1
    n = len(num_str)
    for i in range(n):
        d1 = int(num_str[i])
        for j in range(i + 1, n):
            d2 = int(num_str[j])
            value = 10 * d1 + d2
            if value > best:
                best = value
    return best


puzzle = []

for i in range(200):
    inp = input()
    puzzle.append(inp)

print (f" ans: {joltage(puzzle)}")
            


            

        
            