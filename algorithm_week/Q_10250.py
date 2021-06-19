# ACM 호텔
# 손님들은 정문으로부터 가장 짧은 거리에 있는 방을 선호
# 방 개수 W, 층 수 H, 몇번째 손님 N
# 방번호 YYXX : YY는 층수, XX는 왼쪽부터 방순서

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    floor = n % h
    roomNumber = n // h + 1
    if n % h == 0:
        roomNumber = n // h
        floor = h
    print(f'{floor * 100 + roomNumber}')
