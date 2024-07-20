def solution(s):
    ans = 0
    temp = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            temp+=1
        else:
            if temp > ans:
                ans = temp
            temp = 0
    if temp > ans:
        ans = temp
    return ans + 1


print(solution(input()))