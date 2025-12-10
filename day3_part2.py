def joltage(arr):
    ans = 0
    for s in arr:    
        ans += largest_12(s)
    return ans

def largest_12(num_str):
 
    n = len(num_str)
    result = []
    start = 0 
    k = 12
    for i in range(k):
        end = n - (k - i) 

        window = num_str[start:end + 1]
        max_digit = max(window)            
        offset = window.index(max_digit)   
        chosen_index = start + offset

        result.append(max_digit)
        start = chosen_index + 1

    return int("".join(result))


puzzle = []

for i in range(200):
    inp = input()
    puzzle.append(inp)

print (f" ans: {joltage(puzzle)}")