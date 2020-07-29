'''
1. json 파일 2가지 형식
    1. 중괄호 : {key:value, ...}, {key:value, ...}
        -> json.loads()
    2. 대괄호 : [{key:value, ...}, {key:value, ...}]
        -> json.load()

2. pickle
'''
import json
import pandas as pd
import pickle


# 1. 1번 형식 : 중괄호 {key:value, ...}
# 2. 2번 형식 : 대괄호 [{key:value, ...}]
file = open('./chap07_fileIO/data/labels.json', mode='r', encoding='utf-8')
# print(file.read()) # [{row}, {row}, ...]
rows = json.load(file) # json 문자열 -> python object
print(len(rows)) # 30
#print(rows)
print(type(rows)) # <class 'list'>
for row in rows[:5]:
    print(row)
    print(type(row)) # <class 'dict'>
file.close()
# list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
''' <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 30 entries, 0 to 29
    Data columns (total 5 columns):  '''
print(rows_df.head())


# 2. pickle
''' 
python object(list, dict) -> file(binary) -> python object(list, dict) 
pickle
    save : pickle.dump(data, file) 
    load : pickle.load(file) 
'''

# 2-1) pickle save
file = open('./chap07_fileIO/data/rows_data.pickle', mode='wb') # wb : write binary
pickle.dump(rows, file) # list -> binary <list 가 binary로 저장된다.>
print('pickle file saved')

# 2-2) pickle load
file = open('./chap07_fileIO/data/rows_data.pickle', mode='rb')
rows_data = pickle.load(file)
print(rows_data)
print(type(rows_data)) # <class 'list'>



  




























































