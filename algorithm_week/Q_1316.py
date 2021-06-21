N = int(input())

count = N
for _ in range(N):
    단어 = list(input())
    for i in range(len(단어)-1):
        if 단어[i] == 단어[i+1]:
            pass
        elif 단어[i] in 단어[i+1:]:
            count -= 1
            break
print(count)
