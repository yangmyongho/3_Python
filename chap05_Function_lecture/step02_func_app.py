''' 사용자 정의 함수 응용 '''


# 1. 텍스트 전처리 용도 함수

# 1) clean_text3
def clean_text3(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = [text.lower() for text in texts]
    # 2. 숫자 제거
    texts_re2 = [sub('[0-9]', '', text) for text in texts_re]
    # 3. 문장부호 제거
    punc_str = '[.,:;?!]'
    texts_re3 = [sub(punc_str, '', text) for text in texts_re2]
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*]'
    texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
    # 5. 공백 제거
    texts_re5 = [''.join(text.split()) for text in texts_re4]
    return texts_re5
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(' 텍스트 전처리 전 ')
print(texts)
print(' 텍스트 전처리 후 ')
print(clean_text3(texts))
'''
 텍스트 전처리 전 
['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
 텍스트 전처리 후 
['afabasabag', 'abttaa', 'uysfsfaa']
'''

# 2) clean_text
def clean_text(texts) :
    from re import sub
    # 1. 영문자 제거
    texts_re = sub('[a-z]|[A-Z]','',texts)
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,:;?!]'
    texts_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*]'
    texts_re4 = sub(spec_str, '', texts_re3)
    # 5. 공백 제거
    texts_re5 = ''.join(texts_re4.split())
    return texts_re5
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!',
         '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박',
         '나는 홍길동']
print(' 텍스트 전처리 전 ')
print(texts)
print(' 텍스트 전처리 후 ')
text_re = [clean_text(text) for text in texts]
print(text_re)
'''
 텍스트 전처리 전 
[' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
 텍스트 전처리 후 
['우리나라대한민국우리나라만세', '비아그라정력최고', '나는대한민국사람', '보험료원에평생보장마감임박', '나는홍길동']

'''


# 2. 표본의 분산과 표준편차

from statistics import mean, variance, stdev # 통계 함수
from math import sqrt # 수학 함수
dataset = [2, 4, 5, 6, 1, 8]
print(dataset) # [2, 4, 5, 6, 1, 8]
print(mean(dataset)) # 4.333333333333333
print(variance(dataset)) # 6.666666666666666
print(stdev(dataset)) # 2.581988897471611
print(sqrt(variance(dataset))) # 2.581988897471611

''' 
분산 = sum ( ( x변량 - 평균 )**2 ) / (n-1)
표준편차 = sqrt(분산)
'''

def var_std(dataset) :
    from statistics import mean, variance, stdev
    from math import sqrt
    avg = mean(dataset) # 산술평균
    # 리스트 내포 < list + for >
    dif = [(x-avg)**2 for x in dataset] # ( x변량 - 평균 )**2
    diff_sum = sum(dif)

    var = diff_sum / (len(dataset) - 1) # 분산
    std = sqrt(var) # 표준편차
    return var, std

# 함수 호출
var, std = var_std(dataset)
print('분산 =', var) # 분산 = 6.666666666666666
print('표준편차 =', std) # 표준편차 = 2.581988897471611






























