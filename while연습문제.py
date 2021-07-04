# num = int(input('마지막 숫자를 입력하세요 : '))
# i = 0
# sumi = 0
# while i < num:
#     if i % 2 == 1:
#         sumi = sumi + i
#     i = i+1
# print(sumi)
# while True:
#     num = input('숫자(정수)만 입력하세요, 종료를 원하면 x를 입력하세요: ')
#     if num == 'x':
#         break
#     elif int(num) % 2 == 0:
#         continue
#     else:
#         print('%s는 홀수입니다.' % num)
# print('종료합니다.')
money = 10000
i = 0
while i < 6:
    i = i + 1
    money = money - 2000
    if money != 0:
        print('노래를 %d곡 불렀습니다.' % i)
        print('현재 %d원 남았습니다.' % money)
    elif money == 0:
        print('노래를 %d곡 불렀습니다.' % i)
        break


print('잔액이 없습니다. 종료합니다.')
