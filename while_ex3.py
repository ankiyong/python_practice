
while True:
    num = input('숫자(정수)만 입력하세요, 종료를 원하면 x 를 입력하세요 : ')
    if num == 'x':
        print('종료합니다.')
        break
    elif int(num) % 2 == 0:
        continue
    else:
        print('%s는 홀수입니다.' % num )
