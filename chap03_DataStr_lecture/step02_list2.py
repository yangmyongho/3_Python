'''
리스트 내포
 - list 에서 for문 사용
 형식1) 변수 = [실행문 for 변수 in 열거형 객체]
        실행순서 : 1.for문 -> 2.실행문 -> 3.변수 저장
 형식2) 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]
        실행순서 : 1.for문 -> 2.if문 -> [3.실행문 -> 4.변수 저장]
'''


# 1. 형식1) if문 없는 경우
''' 형식 : 변수 = [실행문 for 변수 in 열거형 객체] '''

# x 각 변량에 제곱
x = [2, 4, 1, 3, 7]
'''' 이렇게 쓰던 식을 짧게 변경할수있음 
data = []
for i in x :
    data.append(i**2)
print(data) # [4, 16, 1, 9, 49] '''
data = [i**2 for i in x] # 한줄로 만듬
print(data) # [4, 16, 1, 9, 49]

# 내장함수 + 리스트 내포 < 각리스트의 합구하기 >
print('sum =', sum(x)) # sum = 17
data4 = [[1, 3, 5], [4, 5], [7, 8, 9]] # 중첩 list
result = [sum(d) for d in data4]
print(result) # [9, 9, 24]


# 2. 형식2) if문 있는 경우
''' 형식 : 변수 = [실행문 for 변수 in 열거형 객체 if 조건식] '''
# 1 ~ 100 -> 3의 배수
num = list(range(1, 101)) # 1 ~ 100
data3 = [i for i in num if i % 3 == 0 ]
print(data3)

 # 리스트내포 에서 참이 아닐때














