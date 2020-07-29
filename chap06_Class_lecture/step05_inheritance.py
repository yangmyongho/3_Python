'''
클래스 상속(Inheritance)
 - 기존(부모) 클래스를 이용해서 새로운(자식) 클래스를 생성하는 문법
 - 부모클래스 정의 -> 자식클래스 생성
 - 상속 대상 : 멤버(o) + 생성자(x)
    -> 생성자는 상속 대상 아님
 형식)
 class 자식클래스(부모클래스) : # class new_class(old_class)
        멤버(변수+메서드)
        생성자
 self  vs  super()
 - self.member : 현재 클래스의 멤버 호출
 - super().member : 부모 클래스의 멤버 호출

'''


# 1-1) 부모클래스
class Super :  # member 3개
    # 멤버변수
    name = None
    age = 0
    # 생성자 : 객체생성+멤버변수초기화
    def __init__(self, name, age): # 부모 생성자
        self.name = name
        self.age = age
    # 멤버메서드 : 데이터처리
    def display(self):
        print('이름 : {}, 나이 : {}'.format(self.name, self.age))

# object 생성
sup = Super('부모', 55)
# object.member()
sup.display() # 이름 : 부모, 나이 : 55


# 1-2) 자식클래스
class Sub(Super) : # member (3+1)개
    # 눈에 보이지않지만 상속이 되어있음
    # name = None <부모멤버>
    # age = 0  <부모멤버>
    # gender = None # 자식에서 추가된 멤버
    def __init__(self, name, age,  gender): # 자식 생성자
        #Super.__init__(self, name, age) # 2차 <둘다 사용가능>
        super().__init__(name, age) # 2차 <둘다 사용가능>
        # self.name = name # 1차
        # self.age = age   # 1차
        self.gender = gender
    def display(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(self.name, self.age,self.gender))

# object 생성
sub = Sub('자식', 22, '남자')
sub.display() # 이름 : 자식, 나이 : 22, 성별 : 남자


# 2-1) 부모클래스 정의
class Parent :
    # 멤버변수
    name = job = None
    # 생성자
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 멤버메서드
    def display(self):
        print('이름 : {}, 직업 : {}'.format(self.name, self.job), end=', ')

parent = Parent('홍길동', '공무원')
parent.display() # 이름 : 홍길동, 직업 : 공무원,


# 2-2) 자식클래스 1 < 방법1) super 키워드 사용 >
class Children1(Parent):
    gender = None
    def __init__(self, name, job, gender):
        super().__init__( name, job) # 부모생성자 호출을통해 초기화
        self.gender = gender # 자식생성자 초기화
    def display(self):
        print('이름 : {}, 직업 : {}, 성별 : {}'.format(self.name, self.job, self.gender))

c1 = Children1('이순신', '군인', '남자')
c1.display() # 이름 : 이순신, 직업 : 군인, 성별 : 남자,
c2 = Children1('유관순', '열사', '여자')
c2.display() # 이름 : 유관순, 직업 : 열사, 성별 : 여자,


# 2-3) 자식클래스 2 < 방법2) 부모클래스로 접근 >
class Chiidren2(Parent):
    gender = None
    def __init__(self, name, job, gender):
        Parent.__init__(self, name, job)
        self.gender = gender
    def plus(self):
        print('성별 : {}'.format(self.gender))
    def display(self):
        Parent.display(self)
        self.plus()

c3 = Chiidren2('김고은', '배우', '여자')
c3.display() # 이름 : 김고은, 직업 : 배우, 성별 : 여자




# 인터넷1 < 방법 : 부모클래스로 접근 >
class father():  # 부모 클래스
    def __init__(self, who):
        self.who = who
    def handsome(self):
        print("{}를 닮아 잘생겼다".format(self.who))

class sister(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def __init__(self, who, where):
        father.__init__(self, who)
        self.where = where
    def choice(self):
        print("{} 말이야".format(self.where))
    def handsome(self):
        father.handsome(self)
        self.choice()

girl = sister("아빠", "얼굴")
girl.handsome()


#인터넷2 < 방법 : super키워드 사용 >
class father():  # 부모 클래스
    def __init__(self, who):
        self.who = who
    def handsome(self):
        print("{}를 닮아 잘생겼다".format(self.who))

class sister(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def __init__(self, who, where):
        super().__init__(who)
        self.where = where
    def choice(self):
        print("{} 말이야".format(self.where))
    def handsome(self):
        super().handsome()
        self.choice()

girl = sister("아빠", "얼굴")
girl.handsome()























































































