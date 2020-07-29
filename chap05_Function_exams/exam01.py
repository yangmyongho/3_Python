'''
문1) Start counter 문제  

height : 3 <- 키보드 입력 
*
**
***
star 개수 : 6
'''

# 함수 정의
def StarCount(height):
    s_cnt = 0  # 별 개수 카운트

    ## 내용 채우기 ##

    return s_cnt


# 키보드 입력
height = int(input('height : '))  # 층 수 입력

# 함수 호출 및 start 개수 출력
print('star 개수 : %d' % StarCount(height))





# # ## 내가한
# 함수 정의
def StarCount(height):
    s_cnt = 0  # 별 개수
    tot = 0 # 별 갯수 카운트
    while True :
        if s_cnt < height:
            s_cnt += 1
            tot += s_cnt
            print('*' * s_cnt)
        else :
            break
    return tot
# 키보드 입력
height = int(input('height : '))  # 층 수 입력
# 함수 호출 및 start 개수 출력
print('star 개수 :', StarCount(height))

 # 선생님
def StarCount1(height):
    s_cnt = 0
    for i in range(height) :
        print('*'*(i+1))
        s_cnt += (i+1)
    return s_cnt
height = int(input('height : '))
print('star 개수 : %d' % StarCount1(height))

print(list(range(5))) # [0, 1, 2, 3, 4]
