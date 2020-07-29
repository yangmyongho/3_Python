'''
문자열 처리
 - 문자열(string) : 문자들의 순서(index) 집합
 - indexing / slicing 가능
 - 문자열 = 상수 : 수정 불가능
'''


# 1. 문자열 처리

# 1) 문자열 유형
# 한 줄 문자열
lineStr = "this is one line string"
print(lineStr)
# 여러줄 문자열
multiStr = '''this is
multi line
string'''
print(multiStr)
multiStr2 = 'this is \nmulti line \nstring' # \n
print(multiStr2)
# sql문 : 부서번호
deptno = int(input('부서번호 입력 :'))
query = f"""select * from emp
where deptno = {deptno}
order by desc"""
print(query)

# 2) 문자열 연산( + 결합, * 반복 )
print('python'+' program') # 결합 연산자
#print('python'+ 37) # 오류  < 형이 같아야함>
print('python'+ str(37)) # python37 < int -> str >
print('-'*30) # 30번 반복
print(37*10) # 숫자형은 곱하기연산자

# 3) 문자열 처리 함수
'''
object.member  or  object.member()
int.member
str.member
'''
print(lineStr, type(lineStr)) # this is one line string <class 'str'>
print('문자열 길이 :', len(lineStr)) # 문자열 길이 : 23
print('문자열 길이 :', lineStr.__len__()) # 문자열 길이 : 23
print('t의 글자수 :', lineStr.count('t')) # t의 글자수 : 2
print(lineStr.upper()) # THIS IS ONE LINE STRING

# 접두어 : 시작문자열
lineStr.startswith('this') # True
print(lineStr.startswith('this')) # True
lineStr.startswith('that') # False
print(lineStr.startswith('that')) # False

# split : 토큰 생성
# 문장 -> 단어
words = lineStr.split(sep=' ')
#words = lineStr.split() # (sep=' ') 생략가능
print(words) # ['this', 'is', 'one', 'line', 'string']
print('단어의 길이 : ', len(words)) # 단어의 길이 :  5
# 문단 -> 문장
sentences = multiStr.split(sep='\n')
#sentences = multiStr.split() # ['this', 'is', 'multi', 'line', 'string'] 띄어쓰기로 나누어짐
print(sentences) # ['this is', 'multi line', 'string']
print('문장의 길이 :', len(sentences)) # 문장의 길이 : 3

# 결합(join) : '구분자'.join(str)
sentence = ' '.join(words)
print(sentence) # this is one line string
para = ','.join(sentences)
print(para) # this is,multi line,string

# 4) indexing / slicing
#lineStr[0] # 't' <첫번째 문자>
print(lineStr[0]) # t
#lineStr[-1] # 'g' <마지막에서 첫번째 문자>
print(lineStr[-1]) # g

print(lineStr[0:4]) # this
print(lineStr[:4]) # this   < [start : end-1]
print(lineStr[-6:]) # string


# 2. escape 문자 처리
'''
escape 문자 : 명령어 이외 특수문자( ', ", \n, \t, \b ) 
'''
print("\nescape 문자") # <줄바꿈뒤에> escape 문자
print("\\nescape 문자") # \nescape 문자 <줄바꿈 x > 두개쓰면 특수기능없는 하나의 문자로인식한다.
print(r"\nescape 문자") # \nescape 문자  <앞에 r 을 쓰면 역슬래쉬 무시한다.>
# C:\python\work\test 같은 경로를 쓸때 역슬래쉬 무시해야한다.
print('C:\python\work\test') # C:\python\work	est 이렇게 나오니까
print(r'C:\python\work\test') # C:\python\work\test r을 넣어서 이렇게 사용해야 한다.
print('C:\\python\work\\test') # C:\python\work\test 또는 이렇게 사용한다.
