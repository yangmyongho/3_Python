'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

# 문1) <실행문을 라인조건식으로 생성>
message = ['spam', 'ham', 'spam', 'ham', 'spam']
dumy = [1 if i =='spam' else 0 for i in message]
print(dumy)


# 문2)
message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list = [d for d in message if d == 'spam' ]
print(spam_list)


# 내가 내는 문제 )   [ 라인if for if문 ]
dumy2 = [1 if i =='spam' else 0 for i in message if len(i) > 2]
print(dumy2) # [1, 0, 1, 0, 1]
dumy3 = [1 if i =='spam' else 0 for i in message if len(i) > 3]
print(dumy3) # [1, 1, 1]
dumy4 = [1 if i =='spam' else 0 for i in message if len(i) > 4]
print(dumy4) # []

