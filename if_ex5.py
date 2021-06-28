'''
도형을 선택해서 면적 구하기
'''

shape_type = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))
if shape_type == 1:
    width = int(input('가로 입력 : '))
    height = int(input('세로 입력 : '))
    square = width * height
    print('사각형의 면적 = ' , square)
elif shape_type == 2:
    width = int(input('가로 입력 : '))
    height = int(input('세로 입력 : '))
    triangle = width * height / 2
    print('사각형의 면적 = ' , triangle)
else:
    radii = int(input('반지름 입력 : '))
    circle = radii **2 * 3.14
    print('원의 면적 = ', circle)
