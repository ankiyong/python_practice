# list_name = []
# for i in range(3):
#     name = input('회원입력 : ')
#     list_name.append(name)
# print('회원명단 :  ',end=" ")
# for i in list_name:
#     print(i,end=" ")
#
# student = 0
# scores = []
# good_std = 0
# n = int(input('학생 수 입력 : '))
# for i in range(n):
#     student += 1
#     score = int(input('학생 %d 점수 입력 : ' % student))
#     scores.append(score)
#     total = sum(scores)
#     avg = total / student
#     if score >= 80:
#         good_std += 1
#     else:
#         pass
# print('총점 : %d' % total)
# print('평균 : %.2f' % avg)
# print('80점 이상 학생 : %d명' % good_std)
# real_product = []
# while True:
#     product = input('상품 등록 (엔터키 누르면 종료) : ')
#     if product == "":
#         break
#     else:
#         real_product.append(product)
# print('등록된 상품 : ',end="")
# for i in real_product:
#     print(i,end=" ")
student = 0
scores = []
good_std = 0
n = int(input('학생 수 입력 : '))
for i in range(n):
    student += 1
    score = int(input('학생 %d 점수 입력 : ' % student))
    scores.append(score)
    total = sum(scores)
    avg = total / student
    if score >= 80:
        good_std += 1
    else:
        pass
scores.sort(reverse=True)
print('총점 : %d' % total)
print('평균 : %.2f' % avg)
print('80점 이상 학생 : %d명' % good_std)
print('점수 내림차순 정렬 : %d', scores)