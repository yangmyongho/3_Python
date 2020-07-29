'''
문2) 다음과 같은 여러 줄의 문자열을 대상으로 정규표현식을
       적용하여 email 양식이 올바른 것만 출력되도록 하시오. 
       
  <email 양식 조건> 
        아이디 : 첫자는 영문소문자, 단어길이 4자 이상
        호스트이름 : 영문소문자 시작, 단어길이 3자 이상 
        최상위 도메인 : 영문소문자 3자리 이하
        
  << 출력 결과 >>
  you2@naver.com
  kimjs@gmail.com
'''

from re import match # match 함수 이용 
# 정규표현식 기본 패턴 : '메타문자@메타문자.메타문자'

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""


# match
result = []
email_list = email.split('\n')

for cor_email in email_list :
    result = match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', cor_email)
    if result :
        print(cor_email)

# 한줄 1)
cor_emails = [print(cor_email) if (match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', cor_email))
             else cor_email for cor_email in email_list]
print(cor_emails)

a = match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', '12kang@hanmail.net')
b = match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', 'kimjs@gmail.com')
print(a)
print(b)

# 한줄 2)
[print(cor_email) if (match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', cor_email)) else cor_email for cor_email in email_list]


# 형이 한거
cor_emails = [cor_email for cor_email in email_list if (match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]{,3}', cor_email))]
for r in cor_emails :
    print(r)

