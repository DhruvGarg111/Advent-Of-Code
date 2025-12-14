def calculate(arr):

    iters = len(arr[-1])
    ans = 0
                
    for i in range(iters):
        if arr[-1][i] == '+':
            cur = 0
            for j in range(len(arr) - 1):
                if i < len(arr[j]):
                    cur += int(arr[j][i])

        elif arr[-1][i] == '*':
            cur = 1
            for j in range(len(arr) - 1):
                if i < len(arr[j]):
                    cur *= int(arr[j][i])

        ans += cur

    return ans

arr = []

while True:
    inp = input()
    if not inp:
        break
    arr.append(inp.split())

print("ans : ", calculate(arr))
