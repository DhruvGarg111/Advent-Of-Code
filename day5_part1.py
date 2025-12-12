def fresh(arr , food):

    ranges = {}
    ans = 0

    for i,j in arr:
        if i not in ranges:
            ranges[i]=j
        else:
            ranges[i] = max(ranges[i],j)

    ranges = dict(sorted(ranges.items(), reverse=True))

    for i in food:
        for j in ranges:
            if i >= j and i <= ranges[j]:
                ans += 1
                break

    return ans


ranges = []
values = []

while True:
    line = input().strip()
    if line == "":
        break
    start, end = map(int, line.split("-"))
    ranges.append([start, end])

while True:

    line = input().strip()
    if line == "":
        break
    values.append(int(line))


print("ans: ", fresh(ranges, values))
