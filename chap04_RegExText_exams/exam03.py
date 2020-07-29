'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    
   <출력 예시> 
유관순 750905-******* 
홍길동 850905-******* 
강감찬 770210-*******  
'''

import re # 정규표현식 패키지 임포트

person = """유관순 750905-2049118
홍길동 850905-1059119
강호동 790101-5142142
강감찬 770210-1542001"""



## 내가한
import re
person_list = person.split('\n')
print(person_list)
result = []
ans = []
for cor_person in person_list :
    result = re.match('\\w{3} [0-9]{6}-[1-4][0-9]{6}', cor_person)
    if result :
        ans = re.sub('[0-9]{7}', '*******',cor_person)
        print(ans)

#






