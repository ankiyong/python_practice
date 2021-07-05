# student = [{'name':'홍길동', 'korean': 87, 'math': 98, 'english': 88, 'science': 95},
#            {'name':'이몽룡', 'korean': 92, 'math': 92, 'english': 96, 'science': 98,},
#            {'name':'성춘향', 'korean': 76, 'math': 76, 'english': 94, 'science': 90,},
#            {'name':'변학도', 'korean': 98, 'math': 92, 'english': 96, 'science': 92,},
#            {'name':'박지성', 'korean': 95, 'math': 98, 'english': 98, 'science': 98,},
#            {'name':'류현진', 'korean': 64, 'math': 88, 'english': 92, 'science': 92,}
#            ]
# print('이름\t','   총점\t','평균')
#
# for i in student:
#     print(i['name'],end="\t")
#     total = i['korean'] + i['math'] + i['english'] + i['science']
#     avg = total/5
#     print(total,end="\t ")
#     print(avg)
eng= {}
while True:
    word = input('영어 단어 등록 (종료는 quit) : ')
    if word in eng:
        print(word+'는 이미 등록된 단어 입니다.')
    elif word == 'quit':
        break
    else:
        kor = input(word+'의 뜻 입력(종료는 quit) : ')
        eng[word] = kor
        if kor == 'quit':
            break
while True:
    search = input('검색할 단어 입력(종료는 quit) : ')
    if search in eng:
        print(search+'의 뜻은'+eng[search]+'입니다.')
    elif search == 'quit':
        print()
        print('종료합니다.')
        break
    else:
        print(search+'는 사전에 없는 단어 입니다.')