# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("data/bcc.csv")
# 사용자 코딩


#1번 문제

#로그 리지스틴값 구하기
df['log_resistin'] = np.log(df['Resistin'])

# 집단 분류
group1 = df[df['Classification']==1]['log_resistin'] #정상
group2 = df[df['Classification']==2]['log_resistin'] #환자
#print(group1.shape, group2.shape)

#F검정 통계량 계산
#두 집단의 분산 구하기
var1 = group1.var()
var2 = group2.var()
#var1 = np.var(group1) 이렇게도 가능. But ddof(자유도)=1  넣어줘야 함! F검정은 샘플검정이기 때문
#df는 알아서 자유도 조정해서 표본분산으로 계산됨

#자유도
dof_1 = len(group1)-1 #집단1의 자유도
dof_2 = len(group2)-1 #집단2의 자유도
#뭐가 더 큰지 출력해서 확인 : 51<63 : 집단2(환자)가 더 큼 => 환자가 분자에 위치!
#print(dof_1, dof_2) 

f_stat = var2/var1

#반올림 소수 셋째자리까지 작성
print(round(f_stat, 3)) #1.348

n1 = len(group1)
n2 = len(group2)
#2번문제: 합동 분산 추정량 
pooled_var = ((n1-1)*var1 + (n2-1)*var2 )/ (n1+n2-2)
print(round(pooled_var, 3)) #0.449

#3번문제: t통계량 구하고 p값 구하기
t_stat = (group1.mean()-group2.mean()) / np.sqrt(pooled_var*(1/len(group1)+1/len(group2)))
#t_stat = (mean1-mean2)/np.sqrt(pooled_var*(1/n1+1/n2))

#p값 구하기
p = 2*(1-stats.t.cdf(abs(t_stat), df=n1+n2-2))
print(round(p, 3)) #0.003
#print(p)

#ttest_result = stats.ttest_ind(group1, group2, equal_var=True) # 등분산 true, default가 True
#print(ttest_result)



# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출
