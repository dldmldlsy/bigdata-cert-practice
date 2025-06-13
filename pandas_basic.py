#판다스100제 
#실제로는 print로 출력해야 함. 구글코랩이라서 print생략된 것.
#항상 괄호 조심하기


#판다스모듈 불러오기
import pandas as pd

#1. 데이터 프레임 생성해서 출력하기
emp = pd.read_csv("파일경로") #파일 읽어서 emp 변수에 담음
emp #출력

#2. 특정 컬럼 출력하기
emp [ ['empno', 'ename', 'sal', 'job']] #특정 컬럼 출력

#3. 특정 검색 조건에 해당하는 데이터 검색하기 
emp[['ename', 'sal', 'job']] [emp['job']=='SALESMAN']
# emp[ 특정 컬럼 리스트 ] [검색조건] => emp[[컬럼명 ,,,]] [emp[컬럼명] 조건식]

#4. 같은 유형 다른 질문: 1200 이상
emp[['ename', 'sal', 'job']] [emp['sal'] >= 1200]

#5. 같은 유형 다른 질문: 부서번호가 20
emp[['ename', 'sal', 'deptno']][emp['deptno']==20]


#기타 다른 연산자로 이뤄진 검색조건
#6. between 
emp[['ename', 'sal']][emp['sal'].between(1000, 3000)]

#7. ~ (Not) : 검색 조건앞에 ~ 붙이기
emp[['ename', 'sal']][~emp['sal'].between(1000, 3000)]

#8. 새로운 csv 파일 가져와서 출력: boston.csv
boston = pd.read_csv("/content/drive/MyDrive/data100/boston.csv")
boston

#9. 특정 조건 검색 + 특정 컬럼명들만 출력
boston[['id', 'price']][boston['price'].between(10, 30)]

#10. 특정 조건 검색 + 모든 컬럼 출력
boston[boston['price'].between(10, 30)]

#인강은 전체 컬럼 출력에 대해 아래 방식으로 알려줌
#답은 맞는데 이건 슬라이싱해서 복사해서 조건필터하는거라 성능적으로 더 비효율적이라고 챗지피티가 말해줌~
boston[:] [boston['price'].between(10, 30)]

#11. 집값이 10~30이 아닌 모든 컬럼 출력
boston[~boston['price'].between(10, 30)]

#12. 한글 섞인 데이터파일 불러와서 출력하기 : emp20.csv 인코딩옵션추가하기
emp20 = pd.read_csv("/content/drive/MyDrive/data100/emp20.csv", encoding= "euckr")
emp20

#13. 나이가 20대인 학생들의 이름, 나이 출력
emp20[['ename', 'age']][emp20['age'].between(20, 29)]

#14. isin : 직업이 둘 중 하나인 사원의 이름, 직업 출력
emp[['ename', 'job']] [emp['job'].isin(['SALESMAN', 'ANALYST'])]

#15. isin : 통신사가 kt, lg인 학생들의 이름, 통신사 출력
emp20[['ename','telecom']][emp20['telecom'].isin(['kt', 'lg'])]

#16. isin + (~) : kt와 lg가 아닌 학생들
emp20[['ename', 'telecom']][~emp20['telecom'].isin(['kt', 'lg'])]


#17. 결측치인 데이터 필터: isnull(), isna()
emp[['ename', 'comm']][emp['comm'].isnull()]
emp[['ename', 'comm']][emp['comm'].isna()]

#엑셀에 결측치인 데이터는 빈칸인데, 파이썬에서 csv파일 불러와서 출력해보면 결측치인 값은 NaN으로 나옴

#18. 결측치가 아닌! : isnull() + (~) , notna()
emp[['ename', 'comm']][~emp['comm'].isnull()]
emp[['ename', 'comm']][emp['comm'].notna()]


# apply, lambda
#19.  이름의 두번째 철자가 M 인 사원들의 이름 출력
emp['ename'][emp['ename'].apply(lambda x : x[1]=='M')]

#20.  이름의 끝글자가 T 로 끝나는 사원들의 이름과 월급을 출력 (끝은 -1)
emp[['ename', 'sal']][emp['ename'].apply(lambda x: x[-1]=='T')]

#21. emp20 테이블에서 성씨가  김씨인 학생들의 이름과 나이를 출력
emp20[['ename', 'age']][emp20['ename'].apply(lambda x : x[0]=='김')]

#22. 성씨가 김씨가 아닌 학생들의 이름과 나이를 출력
emp20[['ename', 'age']][emp20['ename'].apply(lambda x: x[0]!='김')]
emp20[['ename', 'age']][~emp20['ename'].apply(lambda x: x[0]=='김')]


# 데이터 정렬
#23. 조건 검색 + 정렬 : 직업이 판매원인 사원들의 이름, 월급, 직업 출럭 + 월급 내림차순으로
emp[['ename', 'sal', 'job']][emp['job']=='SALESMAN'].sort_values(by='sal', ascending = False)

#24 조건 검색 + 정렬 : 통신사 kt가 아닌 사원들 나이 높은 순으로 이름, 나이, 통신사 출력 
emp20[['ename', 'age', 'telecom']][emp20['telecom']!='kt'].sort_values(by='age', ascending = False)

#코드 한 줄이 너무 길면 변수 할당해서 재사용해도 됨
result = emp20[['ename', 'age', 'telecom']][emp20['telecom']!='kt']
result.sort_values(by='age', ascending = False)


#25.   EMP 데이터 프레임 구조 확인
#시험 환경의 데이터 프레임 어떻게 구성되어있는지 확인하고 시험보는 게 좋음 
emp.info()
#컬럼 데이터 유형 조건 들 확인할 수 있음
#int64: 정수형 숫자
#object: 문자
#float: 실수형 숫자
#hiredate 입사일인데 문자로 저장되어있음! 이걸 날짜로 다루려면 날짜로 변환하는 작업 필요


# 날짜 데이터 다루기
#26.  81년 11월 17일에 입사한 사원들의 이름과 입사일을 출력하시오
emp['hiredate'] = pd.to_datetime(emp['hiredate']) #날짜형으로 변환
emp[['ename', 'hiredate']][emp['hiredate']=='1981-11-17'] #조건에 맞게 검색

#27. 81년도에 입사한 사원들의 이름과 입사일을 출력
emp[['ename', 'job', 'hiredate']][emp['hiredate'].between('1981-01-01', '1981-12-31')]

#28.  직업이 SALESMAN 이고 1981년도에 입사한 사원들의 이름과 직업과 입사일을 출력
# & 연산자로 한번에 두 조건 적용 (& 앞뒤로 꼭 ()로 묶어줘야 함)
emp[['ename', 'job', 'hiredate']][(emp['job']=='SALESMAN') & (emp['hiredate'].between('1981-01-01', '1981-12-31'))]
#나눠서 적용하기
result = emp[['ename', 'job', 'hiredate']][emp['hiredate'].between('1981-01-01', '1981-12-31')]
result[emp['job']== 'SALESMAN']


# 중복 제거 unique
#29. 타이타닉 데이터의 훈련 데이터인 train.csv 를 불러와서  tit 라는 데이터 프레임을 생성
tit = pd.read_csv("/content/drive/MyDrive/data100/train.csv")
tit

#30. 중복 제거해서 컬럼 출력
tit['Pclass'].unique()

#31. 조건 검색 + 중복제거 컬럼 출력
emp['job'][emp['deptno']==20].unique()
# emp[['job']][emp['deptno']==20].unique()  (X)
# 이렇게 대괄호 두개쓰면 데이터프레임형태이므로 시리즈 함수인 unique 적용불가 -> 에러발생

#32.  sk, kt 인 학생들의 나이를 출력하는데 중복 제거
emp20['age'][emp20['telecom'].isin(['sk', 'kt'])].unique()


#문자 함수 다루기
#33. 통신사를 대문자로 출력
emp20['telecom'].str.upper()
emp20.telecom.str.upper()

#34. 이름과 통신사를 출력 + 그 중 통신사를 대문자로 출력
#방법1. 통신사 컬럼을 아예 대문자로 바꿔서 저장하고 다시 출력
emp20['telecom'] = emp20['telecom'].str.upper()
emp20[['ename', 'telecom']]
#방법2. concat으로 두 결과 결합하기
pd.concat([emp20['ename'], emp20['telecom'].str.upper()], axis = 1)
# axis =1: 양옆, axis =0 : 위아래

#35. 이름과 월급 출력 + 이름 소문자
#방법1
emp['ename'] = emp['ename'].str.lower()
emp[['ename', 'sal']]
#방법2
pd.concat([emp['ename'].str.lower(), emp['sal']], axis = 1)

#36. 이름과 월급 출력 + 이름이 scott이고 이름을 소문자로 검색해도 출력되게 *_*
emp[['ename','sal']][emp['ename'].str.lower()=='scott']

#37. 이름과 통신사를 출력 + 통신사를 첫번째대문자 나머지소문자로
#방법1
emp20['telecom'] = emp20['telecom'].str.capitalize()
emp20[['ename', 'telecom']]
#방법2
pd.concat([emp20.ename, emp20.telecom.str.capitalize()], axis=1)

#38. 이름 첫번째부터 두번째 철자까지만 출력
emp['ename'].str.slice(start=0, stop=2)

#39. 성씨가 김씨인 이름, 나이 출력
emp20[['ename', 'age']][emp20.ename.str.slice(0, 1)=='김']

#40. 이름, 나이, 주소 출력 + 서울 거주 X + 나이기준 내림차순
emp20[['ename', 'age']][emp20['address'].str.slice(0, 3)!='서울시'].sort_values(by='age', ascending=False)
#너무 길면 아래처럼 분할
result = emp20[['ename', 'age', 'address']][emp20['address'].str.slice(0, 3)!='서울시']
result.sort_values(by='age', ascending=False)

#len
#41. 이름, 이름 길이 출력 + 이름 길이 긴 순서대로
emp['ename_len'] = emp['ename'].str.len()
emp[['ename', 'ename_len']].sort_values(by='ename_len', ascending=False)

#42. 승객이름, 이름길이 출력 + 이름 길이 긴 순서대로
tit['Name_len'] = tit['Name'].str.len()
tit[['Name', 'Name_len']].sort_values(by = 'Name_len', ascending = False)

#find
#43. 이름에 M 자가 포함된 사원들의 이름과 월급 출력
emp[['ename', 'sal']][emp['ename'].str.find('M')!=-1]
emp[['ename', 'sal']][emp['ename'].str.find('M')>=0]

#44. 이름에 M 자가 포함되지 않은 사원들의 이름과 월급 출력
emp[['ename', 'sal']][emp['ename'].str.find('M')==-1]

#숫자타입 문자타입으로 변환
emp['sal'] = emp['sal'].astype(str)

#replace
#45. 이름과 월급을 출력 + 월급 숫자0을 *로 대체
#오답: sal은 숫자타입이라 str를 쓸 수 없음
emp['sal'] = emp['sal'].str.replace('0', '*')
#오답: sal 값 자체가 0일 때 *로 바꿔주기 때문에 X
emp['sal'] = emp['sal'].replace('0', '*')
#정답
emp['sal_replace'] = emp['sal'].astype(str).str.replace('0', '*')
emp[['ename', 'sal_replace']]
#정답
emp['sal'] = emp['sal'].astype(str)
emp['sal'] = emp['sal'].str.replace('0', '*')
emp[['ename', 'sal']]
#정답
pd.concat([emp['ename'], emp['sal'].astype(str).str.replace('0', '*')],axis=1)

#46. *이 숫자 0인걸 알면 보안위험 -> 월급출력 시 숫자0~3을 *로 대체하기
import re #데이터 전처리 전문 모듈
# re.sub함수 활용 + sal이 원래 숫자형이니까 문자형으로 변환해주는 작업 필요: str(x)
emp['sal_star'] = emp['sal'].apply(lambda x: re.sub('[0-3]', '*', str(x)))
#아니면 아예 아래처럼 문자형으로 변환하는 작업 사전에 하고 람다함수에서는 그냥 x라고 해도 됨.
emp['sal'] = emp['sal'].astype(str) 
emp['sal_star'] = emp['sal'].apply(lambda x: re.sub('[0-3]', '*', x))
#이름이랑 대체한 월급 출력
emp[['ename', 'sal_star']]

#strip
#47. emp.csv 파일에 JACK 데이터를 양쪽에 공백을 넣어 입력 + 이름이 jack 인 이름과 월급 출력
#실제 csv파일 열어서 데이터 추가하고 구글드라이브에 업로드 후 진행 
emp2[['ename', 'sal']][emp2['ename'].str.strip()=='JACK']


#그룹/집계함수

# max

#48. 최대 나이
emp20['age'].max()

#49. 부서번호가 20번인 사원들의 최대 월급
emp['sal'][emp['deptno']==20].max()

#50. 직업이 판매원인 사람들의 최대 월급
emp['sal'][emp['job']=='SALESMAN'].max()

# max + groupby + reset_index
#51. 직업과 직업별 최대 월급
emp.groupby('job')['sal'].max() #이것도 맞지만 
#데이터프레임 형태로 만들어주는 게 보기 좋음
emp.groupby('job')['sal'].max().reset_index()

#52. tit 에서 Pclass 를 출력하고 Pclass 별 최대운임을 출력
tit.groupby('Pclass')['Fare'].max().reset_index()

#53. 통신사, 통신사별 최대나이를 출력. + 최대나이 기준 내림차순
#인덱스가 2 1 0으로 됨 : 이미 데이터프레임을 만들고 거기서 다시 재정렬해서 
emp20.groupby('telecom')['age'].max().reset_index().sort_values(by='age', ascending=False)
#인덱스가 0 1 2: 정렬한 후에 데이터프레임으로 만듦
emp20.groupby('telecom')['age'].max().sort_values(ascending=False).reset_index(name='max_age')

#54. 53번문제 + 컬럼명 변경
result = emp20.groupby('telecom')['age'].max().sort_values(ascending=False).reset_index()
result.colums = ['통신사', '최대나이']
result

# min

#55. 직업, 직업별 최소 얼급 출력 + 최소 월급 오름차순
result = emp.groupby('job')['sal'].min().sort_values(ascending=True).reset_index()
result.columns = ['직업', '최소 월급']
result

#56. 직업, 직업별 최소 월급 + 직업별 최소 월급이 1200 이상인 것만
result = emp.groupby('job')['sal'].min().reset_index()
result[result['sal']>=1200]
#오답: 그룹화한 df랑 뒤에 조건검색할때 쓰이는 emp df랑 달라서 잘못됨
emp.groupby('job')['sal'].min().reset_index()[emp['sal']>=1200]

# sum

#57. 직업, 직업별 토탈월급 출력 + 토탈월급 내림차순
result = emp.groupby('job')['sal'].sum().reset_index().sort_values(by = 'sal', ascending=False)
result.columns = ['직업', '토탈월급']
result

#58. 57번(직업, 직업별 토탈월급 출력 + 토탈월급 내림차순) + 직업이 판매원인 사람 제외
result = emp.groupby('job')['sal'].sum().reset_index().sort_values(by='sal', ascending = False)
result.columns = ['직업', '토탈월급']
result[result['직업']!='SALESMAN']

#59. 58번(직업, 직업별 토탈월급 출력 + 토탈월급 내림차순 + 직업이 판매원) + 직업별 토탈월급이 5000 이상
result = emp.groupby('job')['sal'].sum().reset_index()
result2 = result[(result['job']!='SALESMAN')&(result['sal']>=5000)].sort_values(by='sal', ascending = False)
result2.columns = ['직업', '토탈월급']
result2

# mean 평균값

#60. 입사일에서 년도만 추출
#날짜데이터를 문자형 -> 날짜형으로 변환
emp['hiredate'] = pd.to_datetime(emp['hiredate'])
#년도만 추출
emp.hiredate.dt.year
emp['hiredate'].dt.year #이렇게도 가능

#61. 사원 데이터프레임에 입사년도(hire_year) 컬럼 추가
#입사일에서 입사년도만 추출해서 새로운 컬럼으로 만들어서 넣기
emp['hiredate'] = pd.to_datetime(emp['hiredate'])
emp['hire_year'] = emp['hiredate'].dt.year
emp

#62. 입사년도, 년도별 평균월급 출력
emp['hire_year'] = pd.to_datetime(emp['hiredate']).dt.year
emp.groupby('hire_year')['sal'].mean().reset_index()

#63. 입사년도, 입사년도별 평균월급 출력 + 년도별 평균월급이 높은 순
emp['hire_year'] = pd.to_datetime(emp['hiredate']).dt.year
result = emp.groupby('hire_year')['sal'].mean().reset_index()
result.columns = ['입사한 년도', '평균월급']
result.sort_values(by='평균월급', ascending = False)

# count 카운팅
# 결측치가 있는 데이터는 제외하고 카운트함! -> 결측치가 없는 컬럼으로 카운트하기!

#64 직업, 직업별 인원수 출력 + 직업별 인원수가 3명 이상인 것만
result = emp.groupby('job')['empno'].count().reset_index()
result.columns = ['직업', '인원수']
result[result['인원수']>=3]
