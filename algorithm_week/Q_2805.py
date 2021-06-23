N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾기
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in trees:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)

########################################
# 함수로 풀기

# N, M = map(int, input().split())
# tree = list(map(int, input().split()))
#
#
# def logSum(height):  # 얻어가는 나무 길이 함수
#     totalLog = 0
#     for i in tree:
#         if i - height > 0:
#             totalLog += (i - height)
#
#     return totalLog
#
#
# def binarySearch(targetHeight):  # 이분탐색 함수
#     start, end = 0, max(tree)
#     answer = 0
#     while start <= end:
#         midCutting = (start + end) // 2
#         Sum = logSum(midCutting)
#         if Sum < targetHeight:
#             end = midCutting - 1
#         if Sum >= targetHeight:
#             answer = midCutting
#             start = midCutting + 1
#
#     return answer
#
#
# print(binarySearch(M))
