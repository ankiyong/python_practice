# # for i in range(1,21):
# #     if i % 3 == 0:
# #         print(i,end=" ")
# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
#
# sumi = 0
# for i in range(num1,num2+1):
#     sumi += i
#
# print('%d부터 %d까지의 합 : %d' % (num1,num2,sumi))
# srt_num = int(input('시작숫자를 입력하시오 : '))
# for i in range(srt_num,0,-1):
#     print(i,end=" ")
# print('발사')
#
for i in range(0,4):
    for j in range(0,5):
        print('*',end=" ")
    print()
# for i in range(0,5):
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print()
# n = 5
# for i in range(0,n):
#     for j in range(n,i,-1):
#         print('*',end=" ")
#     print()

# for i in range(0,5):
#     for j in range(i,5):
#         print(' ',end=" ")
#     for j in range(0,i*2+1):
#         print('*',end=" ")
#     print()
# for i in range(0,5):
#     for j in range(0,i):
#         print(' ',end=" ")
#     for k in range(9,i*2,-1):
#         print('*',end=" ")
#     print()
# money = 10000
# song = 2000
# sing = 0
# change = money - (song * sing)
# while sing < 6:
#
#     if change != 0:
#         print('노래를 %d곡 불렀습니다.' % sing)
#         print('현재 %d원 남았습니다.' % (change))
#     else:
#         break
#     sing += 1
#     money = money-song
# print('잔액이 없습니다. 종료합니다.')