import sys

def countNeighbour(arr, i, j):
    rows = len(arr)
    # 8 directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    cnt = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < len(arr[ni]):
            if arr[ni][nj] == '@':
                cnt += 1
    return cnt

def forklift(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '@' and countNeighbour(arr, i, j) < 4:
                ans += 1
    return ans

rolls = []
for _ in range(139):
    line = input()
    rolls.append(list(line.rstrip('\n')))

print(f"ans: {forklift(rolls)}")
