def invalid(arr):
    ans = 0
    for i in range(len(arr)):
        start = int(arr[i].split("-")[0])
        end = int(arr[i].split("-")[-1])

        for k in range(start, end+1):
            if repeated(k):
                ans += k
    
    return ans


def repeated(num):
    s = str(num)
    n = len(s)

    if n % 2 != 0:
        return False

    half = n // 2
    return s[:half] == s[half:]


pattern = input()
print(invalid(pattern.split(",")))