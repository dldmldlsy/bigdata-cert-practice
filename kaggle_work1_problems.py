# 캐글 작업형1 예상 문제

# [py] T1-1. 이상치를 찾아라(IQR활용)
# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오

import pandas as pd

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/Titanic.csv")

#print(df['Fare'])

q1 = df['Fare'].quantile(0.25)
q3 = df['Fare'].quantile(0.75)
iqr = q3-q1

result = df[(df['Fare']<(q1-1.5*iqr))|(df['Fare']>(q3+1.5*iqr))]
cnt = result['Gender'][result['Gender']=='female'].count()
#cnt len(result[result['Gender']=='female'])
print(cnt)



# [py] T1-2. 이상치를 찾아라(소수점 나이)
# 주어진 데이터에서 이상치(소수점 나이)를 찾고 
# 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오

import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
# print(df['age'][df['age'].apply(lambda x : x%1 !=0)])
result = df['age'][df['age']%1!=0].reset_index()
result['올림'] = np.ceil(result['age'])
result['내림'] = np.floor(result['age'])
result['버림'] = np.trunc(result['age'])
print(result)

age_mean = result['올림'].mean() + result['내림'].mean()+result['버림'].mean()
print(age_mean)



# [py] T1-3. 결측치 처리(map 활용)
# 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 
# 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요

import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")

#print(len(df)-df.count()) #각 컬럼 결측치 개수 구하기
result = df.isnull().sum()/len(df)
#print(result)
result2 = result[result>=0.8]
drop_columns= result2.index
df.drop(drop_columns, axis=1, inplace=True)
print(df)
#방법1
#df['f1'] = df['f1'].fillna(df.groupby('city')['f1'].transform('median'))
#print(df['f1'].mean())

#방법2
print(df['city'].unique())

s = df['f1'][df['city']=='서울'].median()
b = df['f1'][df['city']=='부산'].median()
d = df['f1'][df['city']=='대구'].median()
g = df['f1'][df['city']=='경기'].median()


df['f1'] = df['f1'].fillna(df['city'].map({'서울': s, '경기': k, '부산': b, '대구': d}))

df['f1'].mean()



# [py] T1-5. 조건에 맞는 데이터 표준편차 구하기
# 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오

import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
enfj_std = df['f1'][df['f4']=='ENFJ'].std()
infp_std = df['f1'][df['f4']=='INFP'].std()
print(abs(enfj_std-infp_std))



# [py] T1-6. 결측치 제거 및 그룹 합계
# 주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고, 
# 'city'와 'f2'을 기준으로 묶어 합계를 구하고, 
# 'city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값을 구하시오

import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
drop_index = []
for i in df.index:
    if(pd.isnull(df.loc[i, 'f1'])):
        drop_index.append(i)
drop_index
df.drop(drop_index, axis = 0, inplace=True)

result = df.groupby(['city', 'f2'])['f1'].sum().reset_index()
print(result['f1'][(result['city']=='경기')&(result['f2']==0)].iloc[0])



# [py] T1-7. 값 변경 및 2개 이상의 조건
# 'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 
# 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오

import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")

df['f4'] = df['f4'].str.replace('ESFJ', 'ISFJ')
df['age'][(df['city']=='경기')&(df['f4']=='ISFJ')].max()



# [py] T1-9. 수치형 변수 표준화
# 주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오

#첫풀이
import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
df['stand_f5'] = (df['f5']-df['f5'].mean())/df['f5'].std()
print(df['stand_f5'].median())

##ddof설정
import pandas as pd
import numpy as np

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/basic1.csv")
df['stand_f5'] = (df['f5']-df['f5'].mean())/df['f5'].std(ddof=0)
print(df['stand_f5'].median())


## ddof=0 넣어주면 모집단 표준편차로 작용됨

## 또다른 풀이
# 표준화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['f5']=scaler.fit_transform(df[['f5']])
print(df['f5'].median())
