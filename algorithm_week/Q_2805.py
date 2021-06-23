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

N, M = map(int, input().split())
tree = list(map(int, input().split()))


# 원하는 나무의 양을 target에 대입.
# start, mid , end := 톱의 높이
def logSum(height):
    totalLog = 0
    for i in tree:
        if i - height > 0:
            totalLog += (i - height)

    return totalLog


def binarySearch(targetHeight):
    start, end = 0, max(tree)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        Sum = logSum(mid)
        if Sum < targetHeight:
            end = mid - 1
        if Sum >= targetHeight:
            ans = mid
            start = mid + 1

    return ans


print(binarySearch(M))
