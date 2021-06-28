'''
정수 2개를 입력 받아서 두 수 사이의 합을 구하는
프로그램을 작성 (for문 사용)
'''

num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))

sumi = 0
for i in range(num1,num2+1):
    sumi = sumi + i
print('%d부터 %d까지의 합 : %d' % (num1,num2,sumi))