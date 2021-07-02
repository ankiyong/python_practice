def order():
    price = int(input('상품가격 입력 : '))
    ea = int(input('주문수량 입력 : '))
    total = price*ea
    return price,ea,total
a,b,c = order()
print('------------------------------')
print('상품가격 : %d원' % a)
print('주문수량 : %d개' % b)
print('주문액 : %d원' % c)
