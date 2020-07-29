'''
csv, excel file read/write
 - 칼럼 단위로 작성된 파일 유형

cmd에서 외부 라이브러리 설치
 csv : pip install pandas
 excel : pip install xlrd
'''
import pandas as pd # as 별칭
import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspacek



# 1. csv file read
spam_data = pd.read_csv('./chap07_FileIO/data/spam_data.csv', header=None, encoding='ms949')
print(spam_data.info()) # str()과 비슷
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4   관측치       <5개관측치>
Data columns (total 2 columns): 칼럼(0,1)    <열의개수 :2개>
'''
print(spam_data)

# 1-2) x,y 변수 선택
target = spam_data[0] # DF[칼럼명]
texts = spam_data[1] # DF[칼럼명]
print(target) # Name: 0, dtype: object
print(texts) # Name: 1, dtype: object

# 1-3) target -> dimmy
target = [1 if x == 'spam' else 0 for x in target]
print(target) # [0, 1, 0, 1, 0]

# 1-4) text 전처리
def clean_text(texts) :
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)
    # 5. 영문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4)
    # 5. 공백 제거
    texts_re6 = ' '.join(texts_re5.split())
    return texts_re6
clean_texts = [clean_text(text) for text in texts]
print('텍스트 전처리 전 :\n', texts)
print('텍스트 전처리 후 :', clean_texts)


# 2. csv file read 2
# 2-1) bmi.csv
bmi = pd.read_csv('./chap07_FileIO/data/bmi.csv', encoding='utf-8')
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
'''
print(bmi.head()) # 앞부분 5개 관측치
print(bmi.tail()) # 뒷부분 5개 관측치
height = bmi['height'] # DF['칼럼명']
weight = bmi['weight'] # DF['칼럼명']
label = bmi.label # DF.칼럼명
print(len(height)) # 20000
print(len(label)) # 20000

# 2-2) 평균
print('키 평균 :', height.mean()) # 키 평균 : 164.9379
print('몸무게 평균 :', weight.mean()) # 몸무게 평균 : 62.40995

# 2-3) min/max
max_h = max(height)
max_w = max(weight)
print('키가 제일 큰 사람 :', max_h) # 키가 제일 큰 사람 : 190
print('몸무게가 제일 큰 사람 :', max_w) # 몸무게가 제일 큰 사람 : 85

# 2-4) 정규화
height_nor = height / max_h
weight_nor = weight / max_w
print(height_nor.mean()) # 0.8680942105263159
print(weight_nor.mean()) # 0.734234705882353

# 2-5) 범주형 변수 : label
label_cnt = label.value_counts() # 빈도수 확인
print(label_cnt)
''' normal   7677    /    fat   7425    /    thin   4898 '''


# 3. excel file read
excel = pd.ExcelFile('./chap07_FileIO/data/sam_kospi.xlsx')
print(excel) # object info
kospi = excel.parse('sam_kospi')
print(kospi.info()) # 정보
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
'''
print(kospi) # 내용


# 3. csv file save
kospi['Diff'] = kospi.High - kospi.Low # 파생변수
print(kospi.info()) # Data columns (total 7 columns):
# csv file 저장 : 행 번호 제외
kospi.to_csv('./chap07_FileIO/data/kospi_df.csv', index=None, encoding='utf-8')
# csv file 읽기
kospi_df = pd.read_csv('./chap07_FileIO/data/kospi_df.csv', encoding='utf-8')
print(kospi_df.head())
'''
         Date     Open     High      Low    Close  Volume   Diff
0  2015-10-30  1345000  1390000  1341000  1372000  498776  49000
1  2015-10-29  1330000  1392000  1324000  1325000  622336  68000
2  2015-10-28  1294000  1308000  1291000  1308000  257374  17000
3  2015-10-27  1282000  1299000  1281000  1298000  131144  18000
4  2015-10-26  1298000  1298000  1272000  1292000  151996  26000
'''












