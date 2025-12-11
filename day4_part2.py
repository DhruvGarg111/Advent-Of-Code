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

def forklift():
    global rolls
    ans = 0
    free = []
    for i in range(len(rolls)):
        for j in range(len(rolls[i])):
            if rolls[i][j] == '@' and countNeighbour(rolls, i, j) < 4:
                ans += 1
                free.append((i,j))

    for m,n in free:
        rolls[m][n] = '.'

    return ans


rolls = []
for _ in range(139):
    line = input()
    rolls.append(list(line.rstrip('\n')))

answer = 0

while True:
    removed_count = forklift()
    if removed_count == 0:
        break
    answer += removed_count

print(f"ans: {answer}")
