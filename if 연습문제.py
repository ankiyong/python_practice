# # x = 3
# # y = x**3 + 3 * x**2 + 7 * x + 10
# # print(y)
# # ID = 'flower'
# # PW =  1234
# #
# # input_id = input('아이디 입력 : ')
# # input_pw = int(input('비밀번호 입력 : '))
# #
# # if input_id == ID and input_pw == PW:
# #     print('로그인 성공! ')
# # else:
# #     print('로그인 실패!')
# # weight = eval(input('짐의 무게는 얼마입니까 ? : '))
# # charge = 20000
# # if weight > 20:
# #     print('무게 초과. 수수료 %s원' % format(charge,','))
# # else:
# #     print('수수료 없음')
# # print('종료합니다.')
# # num = int(input('정수 입력 : '))
# # if num % 2 == 0:
# #     print('짝수')
# # else:
# #     print('홀수')
# # num1 = int(input('정수1 입력 : '))
# # num2 = int(input('정수2 입력 : '))
# # num3 = int(input('정수3 입력 : '))
# # if num1 > num2 and num1 > num3:
# #     print('제일 큰 수 : %d' % num1)
# # elif num2 > num3:
# #     print('제일 큰 수 : %d' % num2)
# # else:
# #     print('제일 큰 수 : %d' % num3)
# #
# # shape = ""
# # type = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))
# # if type == 1:
# #     w = int(input('가로 입력 : '))
# #     h = int(input('세로 입력 : '))
# #     area = w * h
# #     shape = '사각형'
# #
# # elif type == 2:
# #     w = int(input('밑변 입력 : '))
# #     h = int(input('높이 입력 : '))
# #     area = (w * h) / 2
# #     shape = '삼각형'
# #
# # else:
# #     r = int(input('반지름 입력 : '))
# #     area = r**2 * 3.141592
# #     shape = '원'
# #
# # print('%s의 면적 = %.2f' % (shape,area))
#
# product_num = int(input('상품 번호 입력 : '))
# if product_num == 1:
#    product_ea = int(input('주문 수량 입력 : '))
#    name = '노트북'
#    price = 1200000
# elif product_num == 2:
#    product_ea = int(input('주문 수량 입력 : '))
#    name = '디지털카메라'
#    price = 400000
# money = price * product_ea
# if money >= 1000000:
#     dc = money * 0.1
# elif money >= 500000:
#     dc = money * 0.05
# amount = money - dc
# print('**********상품 정보**********\n'
#       '1 노트북 : 1,200,000 원\n'
#       '2 디지털카메라 : 400,000 원')
# print('상품명 : \t %s' % name)
# print('가격 : \t\t %s' % format(price,','))
# print('주문 수량 : \t %d' % product_ea)
# print('주문액 : \t %s원 ' % format(int(money),','))
# print('할인액 : \t %s원' % format(int(dc),','))
# print('총지불액 : \t %s원' % format(int(amount),','))