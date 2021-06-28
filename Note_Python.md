# 모르는 것_Python

1.for문 작성 시 반복횟수 제한

```
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))

sumi = 0
for i in range(num1,num2+1):
    sumi = sumi + i
print('%d부터 %d까지의 합 : %d' % (num1,num2,sumi))
```

2.출력 옵션

```
srt_num = int(input('시작 숫자를 입력하시오: '))
for i in range(srt_num,0,-1):
    print(i,end=" ")
print('발사')
```

=> 시작 숫자를 입력하시오: 5
5 4 3 2 1 발사

=> 기본형으로 출력 시 

시작 숫자를 입력하시오: 5
5
4
3
2
1
발사