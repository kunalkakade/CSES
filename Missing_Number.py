def solution(n, arr):
    ssum = n*(n+1)/2
    return int(ssum - sum(arr))

print(solution(int(input()),map(int,input().split())))