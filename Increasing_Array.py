def solution(arr):
    moves = 0
    for i in range(1, len(arr)):
        diff = arr[i-1] - arr[i]
        # print(diff)
        if diff > 0:
            moves += diff
            arr[i]+= diff
    return moves

lenn = input()
arr_str = input().split()
arr = list(map(int, arr_str))
print(solution(arr))