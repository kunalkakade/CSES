def solution(n):
    ans = [n]
    while n !=1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        ans.append(n)
    return ans


aa = solution(int(input()))
print(" ".join(map(str, aa)))