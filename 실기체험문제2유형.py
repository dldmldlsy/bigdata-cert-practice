# 빅분기 실기 2유형 체험 환경 문제
import pandas as pd

train = pd.read_csv("data/customer_train.csv")
test = pd.read_csv("data/customer_test.csv")

# 사용자 코딩
#1. 데이터 유형 파악
#info 해서 나오는 non-null수로 결측치 여부 확인가능
#print(train.info())
#print(test.info())

#2. 데이터 전처리
#(1) 독립변수, 종속변수 나눠주기: X, Y, train/test set 분리
x_train = train.drop(['회원ID','총구매액'], axis=1) 
#총구매액은 우리가 예측해야하니까 제거, 회원ID는 각 데이터 고유한 값이라 오히려 과적합될 수 있어서 제외
y = train['총구매액'] #종속변수
x_test = test.drop(['회원ID'], axis = 1) #테스트데이터는 왜 다루는거지??

#shape 확인하는 습관 추천

#print(x_train.shape, y.shape, x_test.shape)

#(2) 결측치 처리
# 환불금액에 결측치 있음. 결측치 처리 방법 다양한데, 아예 날리는 건 너무 위험함. 
# 평가데이터 결측치도 날려버리면 안됨 -> 제출시 2482개 데이터 그대로 제출해야함
# 그럼 뭘로 채워넣지? 환불금액 결측치 => 환불을 하지 않았다! 는 거니까 0으로 채워넣는 것이 타당하다고 판단.
x_train['환불금액'] = x_train['환불금액'].fillna(0)
x_test['환불금액'] = x_test['환불금액'].fillna(0)

#결측치 개수 확인해보기 : 잘 처리 됐는지~
#print(x_train.isna().sum())
#print(x_test.isna().sum())

#(3) 수치형 변수 스케일링
#스케일링? 데이터 수치 범위 조정
#수치형 변수 스케일링 = 범주형(문자형) 제외하고 수치형 컬럼들에 대해서 스케일링 적용한다
# 수치형 변수 스케일링 방법 두가지(보다 더 있긴 함): minmax, standard
# 여기선 MinMaxScaler 사용

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
# 주구매상품, 주구매지점 말고 수치형 변수임 지금.
# 수치형 변수들을 이렇게 다 적어줘도 되지만 : x_train[['최대구매액', '환불금액',,,]]
num_columns = x_train.select_dtypes(exclude='object').columns
#print(num_columns)

#fit(min, max 등 계산), transform(계산한 값 기준으로 스케일링 적용)
x_train[num_columns] = scaler.fit_transform(x_train[num_columns])
x_test[num_columns] = scaler.transform(x_test[num_columns])

#(4) 범주형 변수 인코딩
#train에 없는데 test에 있는 문자데이터에 대해서 문제가 발생..! 
#그래서 미리 확인 필요 : set() 활용! 
#print(set(x_test['주구매상품'])-set(x_train['주구매상품']))
#set()이라고 나옴 = 아무것도 안나옴 => test에 있는 주구매상품범주들이 train에도 다 존재한다는 의미

# #반대로 한번 해보겠음
# print(set(x_train['주구매상품'])-set(x_test['주구매상품']))
# # {'소형가전'} 이라고 나옴! => train에는 소형가전이 있는데 test에는 없음
#print(set(x_train['주구매지점'])-set(x_test['주구매지점']))
## 얘도 빈 set이 나왔음

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

x_train['주구매상품'] = encoder.fit_transform(x_train['주구매상품'])
x_test['주구매상품'] = encoder.transform(x_test['주구매상품'])

x_train['주구매지점'] = encoder.fit_transform(x_train['주구매지점'])
x_test['주구매지점'] = encoder.transform(x_test['주구매지점'])

#전처리 끝!

#3. 데이터 분리
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x_train, y, test_size=0.2)
#print(x_train.shape, x_val.shape, y_train.shape, y_val.shape)
# (2800, 8) (700, 8) (2800,) (700,) 8:2로 잘 분리됨!

# 4. 모델 학습 및 검증
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor() #모델 생성
model.fit(x_train, y_train) # 학습시킴
y_val_pred = model.predict(x_val) # 검증용데이터 정답을 예측한 값

# 5. 평가
# 평가지표: RMSE
from sklearn.metrics import root_mean_squared_error, r2_score
rmse = root_mean_squared_error(y_val, y_val_pred) #실제값, 예측값
r2 = r2_score(y_val, y_val_pred)
print(rmse, r2)

# 6. 결과 저장
y_pred = model.predict(x_test)
result = pd.DataFrame(y_pred, columns=['pred'])
result.to_csv('result.csv', index=False)

# 7. 결과 확인
result = pd.read_csv('result.csv')
print(result)
