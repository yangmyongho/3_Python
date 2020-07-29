'''
1. private 변수 = 클래스 내의 은닉변수
    object.member : 객체 -> 은닉변수(x)
    getter() / setter() -> 은닉변수(o)
2. class 포함관계(inclusion)
    - 특정 객체가 다른 객체를 포함하는 클래스 설계 기법
    - 두 객체 간의 통신 지원
    ex) class A(a) <-> class B(b)
'''


# 1. private 변수
class Login : # vid, pwd -> db['hong', '1234' 저장
    # 생성자
    def __init__(self, uid, pwd):
        # 형식) self.__private = 변수
        self.__dbId = uid
        self.__dbPwd = pwd

    # getter() : 획득자(return)
    def getIdPwd(self):
        return self.__dbId, self.__dbPwd

    # setter() : 지정자(인수)
    def setIdPwd(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd

# object
login = Login('hong', '1234')
# object.member
# print(login.__dbId) # AttributeError: 'Login' object has no attribute '__dbId'
# 중요한변수이므로 외부에서 볼수없고 수정할수없게 만든것 = 은닉변수
login.getIdPwd() # ('hong', '1234')
uid, pwd = login.getIdPwd()
print('id : {}, pwd : {}'.format(uid, pwd)) # id : hong, pwd : 1234
login.setIdPwd('lee', '5678') # 수정
login.getIdPwd() # ('lee', '5678')
uid, pwd = login.getIdPwd()
print('id : {}, pwd : {}'.format(uid, pwd)) # id : lee, pwd : 5678


# 2. class 포함관계(inclusion)
''' class A(a) <-> class B(b) '''
class Server :
    # 기본생성자

    # 멤버메서드
    def send(self, obj): # object 인수로 받음
        self.obj = obj # 멤버변수 생성
    # 인증메서드
    def cert(self, uid, upwd): # 사용자(id/pwd)
        dbId, dbPwd = self.obj.getIdPwd() # getter 호출
        if dbId == uid and dbPwd == upwd :
            print('로그인 성공~~~')
        else:
            print('로그인 실패~~~')

server = Server()
server.send(login)
server.cert('hong', '1234') # 로그인 실패~~~
server.cert('lee', '1234') # 로그인 실패~~~
server.cert('hong', '5678') # 로그인 실패~~~
server.cert('lee', '5678') # 로그인 성공~~~

































































