c = int(input())  # 케이스 수 입력

for _ in range(c):
    count = 0  # 평균을 넘는 학생수
    점수들 = list(map(int, input().split()))  # 점수 개수 및 점수들 리스트로 입력
    평균점수 = sum(점수들[1:]) / 점수들[0]  # 리스트 받은 것 슬라이싱 / 점수 개수
    for 점수 in 점수들[1:]:  # 판단
        if 점수 > 평균점수:
            count += 1
    비율 = count / 점수들[0] * 100  # 평균이상인 학생수 비율
    print(f'{비율:.3f}%')  # 소수점 셋째 자리까지 출력