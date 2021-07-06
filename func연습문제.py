# def sum():
#     num1 = int(input('숫자1 입력 : '))
#     num2 = int(input('숫자2 입력 : '))
#     return num1 + num2
# a = sum()
# print('합 : %d' % a)
# def get_area():
#     width = int(input('가로 길이 입력 : '))
#     height = int(input('세로 길이 입력 : '))
#     area = width * height
#     return area
#
# a = get_area()
# print('사각형의 면적 : %d' % a)
def get_interest():
    deposit = int(input('예금액 입력 : '))
    int_rate = float(input('이자율 입력(%) : '))

    interest = deposit*int_rate/100

    return  interest
a = get_interest()
print('이자액 : %d원' % a)



def order(pr,qt):

    amount = price * qty
    if amount >= 100000:
        discount = amount * 0.1
    elif amount >= 50000:
        discount = amount * 0.05
    total = amount - discount
    return amount, discount, total

price = int(input('상품가격 입력 : '))
qty = int(input('주문수량 입력 : '))
pr,ea,total = order()


print('상품가격 : %d원' % pr)
print('주문수량 : %d개' % ea)
print('주문액 : %d원' % total)