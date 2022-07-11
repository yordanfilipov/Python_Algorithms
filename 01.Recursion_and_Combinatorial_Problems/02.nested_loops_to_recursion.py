def gen01(idx, vector, n):
    if idx >= len(vector):
        print(*vector, sep=" ")
        return
    for num in range(1, n + 1):
        vector[idx] = num
        gen01(idx + 1, vector, n)


n = int(input())
vector = [1] * n

gen01(0, vector, n)