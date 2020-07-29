'''
set 특징
 - 순서 없음(index 사용 불가)
 - 중복 허용 불가
 - 집합 개념
 형식) 변수 = {값1, 값2, ...}
'''

s = {1, 3, 5}
print(s, type(s), len(s)) # {1, 3, 5} <class 'set'> 3
s = {1, 3, 5, 1} # 1을 또 넣어도 입력하지않음 <중복 불가>
print(s, type(s), len(s)) # {1, 3, 5} <class 'set'> 3
for d in s :
    print(d, end=' ') # 1 3 5
s2 = {3, 6}

# 집합 관련 함수
print(s.union(s2)) # {1, 3, 5, 6}  < 합집합 >
print(s.difference(s2)) # {1, 5}  < 차집합 >
print(s.intersection(s2)) # {3}  < 교집합 >


# list : gender
gender = ['남자', '여자', '남자', '여자'] # 중복 허용

# list -> set
sgender = set(gender) # 중복 불가
print(sgender) # {'여자', '남자'}
# (index 사용불가)
# print(sgender[0])

# set -> list
lgender = list(sgender) # 중복 가능
print(lgender) # ['여자', '남자']
# (index 사용가능)
print(lgender[0]) # 여자


# 원소 추가 / 삭제   <수정과삽입은 index갑 없어서 추가와 같음>
s3 = {1, 3, 5, 7}
s3.add(9) # 원소 추가
print(s3) # {1, 3, 5, 7, 9}
s3.discard(3) # 원소 삭제
print(s3) # {1, 5, 7, 9}





















