'''
step05 문제 

 문) 다음 movie 객체를 대상으로 평점 8이상인 영화 제목과 누적관객수를 출력하시오.

 <출력 결과>
 영화제목 : 광해
 영화제목 : 관상
 누적 관객수 =  2,100
'''
 
movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500], '관상' : [8.01, 900]}

# 내가한 1
for i in movie :
    print(i, end=' : ')
    print(movie[i])
# 내가한 2
su = 0
for i in movie.keys() :
    if movie[i][0] > 8 :
        print('영화제목 :', i)
        su += movie[i][1]
print('누적 관객수 =', format(su, '3,d'))






