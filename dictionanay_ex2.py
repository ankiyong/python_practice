dict = {}
while True:
    eng = input('영어 단어 등록 (종료는 quit) : ')

    if eng == 'quit':
        break
    elif eng not in dict:
        word = input(eng+'의 뜻 입력 (종료는 quit) : ')
        dict[eng] = word
    else:
        print('%s는 이미 등록된 단어 입니다.' % eng)

while True:
    search = input('검색할 단어 입력 (종료는 quit) : ')
    if search == 'quit':
        break
    elif search in dict:
        print('%s의 뜻은 %s입니다.' % (search,dict[search]))
    else:
        print('%s는 사전에 없는 단어 입니다.' % search)