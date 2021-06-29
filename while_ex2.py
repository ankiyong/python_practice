num = int(input('마지막 숫자를 입력하세요 : '))
sun_num = 0
i = 1
while i < num:
    i += 1
    if i % 2 == 1:
        sun_num += i
print('%d부터 %d까지의 홀수의 합은 %d 입니다. ' % (i,num,sun_num))
