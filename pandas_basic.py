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
