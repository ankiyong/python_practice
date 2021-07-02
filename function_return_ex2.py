def get_area():
    width = int(input('가로길이 입력 : '))
    heitht = int(input('세로길이 입력 : '))
    area = width*heitht
    return area

a = get_area()
print('사각형의 면적 : %d' % a)