song_per = 2000
money = 10000
i = 0
while i < 5:
    i += 1
    money -= song_per
    print('%d곡 불렀습니다' % i)
    if money == 0:
        break
    print('현재 %d원 남았습니다.' % money)

print('잔액이 없습니다. 종료합니다.')