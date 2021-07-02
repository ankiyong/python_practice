student = [{'name':'홍길동', 'korean': 87, 'math': 98, 'english': 88, 'science': 95},
           {'name':'이몽룡', 'korean': 92, 'math': 92, 'english': 96, 'science': 98,},
           {'name':'성춘향', 'korean': 76, 'math': 76, 'english': 94, 'science': 90,},
           {'name':'변학도', 'korean': 98, 'math': 92, 'english': 96, 'science': 92,},
           {'name':'박지성', 'korean': 95, 'math': 98, 'english': 98, 'science': 98,},
           {'name':'류현진', 'korean': 64, 'math': 88, 'english': 92, 'science': 92,}
           ]

print('이름\t','총점\t','평균\t')

for i in student:
    total = i['korean'] + i['math'] + i['english']+i['science']
    avg = total/4
    print(i['name'],total,avg)