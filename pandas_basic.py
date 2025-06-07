#판다스100제 
#실제로는 print로 출력해야 함. 구글코랩이라서 print생략된 것.

#판다스 불러오기
import pandas as pd

#1. 데이터 프레임 생성해서 출력하기
emp = pd.read_csv("파일경로") //파일 읽어서 emp 변수에 담음
emp //출력

#2. 특정 컬럼 출력하기
emp [ ['empno', 'ename', 'sal', 'job']] // 특정 컬럼 출력

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

#인강은 전체 컬럼 출력에 대해 아래 방식으로 알려줌 ㅇㅇ 
#답은 맞는데 이건 슬라이싱해서 복사해서 조건필터하는거라 성능적으로 더 비효율적이라고 챗지피티가 말해줌~
boston[:] [boston['price'].between(10, 30)]

#11. 집값이 10~30이 아닌 모든 컬럼 출력
boston[~boston['price'].between(10, 30)]

#12. 한글 섞인 데이터파일 불러와서 출력하기 : emp20.csv 인코딩옵션추가하기
emp20 = pd.read_csv("/content/drive/MyDrive/data100/emp20.csv", encoding= "euckr")
emp20


#13. 나이가 20대인 학생들의 이름, 나이 출력
emp20[['ename', 'age']][emp20['age'].between(20, 29)]
