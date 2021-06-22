N = num = int(input())  # N = 26

count = 0
while True:
    first_digit = num // 10  # 2
    second_digit = num % 10  # 6
    a = (first_digit + second_digit) % 10  # 8
    total_number = int(str(second_digit) + str(a))  # 68 = "6" + "8"
    if N == total_number:  # 26
        count += 1
        print(count)
        break
    else:
        num = total_number
        count += 1