def fresh(arr):

    arr.sort(key=lambda x: x[0])

    merged = []
    
    if arr:
        merged.append(arr[0])

    for current_start, current_end in arr[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end:
            merged[-1][1] = max(last_end, current_end)
        else:
            merged.append([current_start, current_end])

    ans = 0
    for start, end in merged:
        ans += ((end - start) +1)

    return ans


ranges = []

while True:
    line = input().strip()
    if line == "":
        break
    start, end = map(int, line.split("-"))
    ranges.append([start, end])


print("ans: ", fresh(ranges))
