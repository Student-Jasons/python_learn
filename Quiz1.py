# while문을 사용하여 1부터 1000까지의 자연수중 3의 배수의 합을 구해보자 (난이도 하) (못풀면 수학 1학년보다 못하는거)
# i = 1
# result = 0
# while i <= 1000: # i 가 1000보다 작거나 같을때까지 반복
#     if i % 3 == 0: # 만약 i를 3으로 나누었을때 나머지가 0이라면
#         # print(i)
#         result = result + i #결과 변수에 i 더하기
#     i=i+1 #i숫자 1올림 (누적)
# print(result) #결과변수 출력
# -------------------------------------
# while문을 사용하여 다음과 같이 별을 표시하는 프로그램을 작성해보자 (난이도 중)
# 출력예시
# *
# **
# ***
# ****
# *****
# i = 1
# while i<=5: # i가 5보다 작거나 작지 않을때까지 반복
#     for i2 in range(1,i+1): # i만큼 반복
#         print("*", end="") # 별 출력 (end를 써주어 줄바꿈 돼지 않게 함)
#     print("") # \n대용
#     i=i+1 # i에 1 누적

# --------------------------------------------
# for문을 사영하여 1부터 100까지 숫자 출력 (난이도 : 최저)
# for i in range(1,101): # 1-100까지 반복하고 순차적으로 i에추가
#     print(i)# i출력
# for i in range(1,101): print(i) #1줄로 가능
# 코드 30자임 공백 포함해서.
# 1줄로 가능 ㅋㅋ
# ------------------------------------------
# a학급에 총 10명이 있다. 이 학생들의 중간고사 점수는 다음과 같다
# [중간고사 점수]
# [70,60,55,75,95,90,80,80,85,100]
# for문 이용하여 a학급 평균내기 (난이도 : 중)
# data = [70,60,55,75,95,90,80,80,85,100] # 중간고사 성적
# result = 0# 총 합
# for i in data:# data만큼 반복하고 data변수 내용을 i에 순차적으로 대임
#     result = result + i #result변수에 i더함
# print(int(result/(len(data)))) # result변수를 data변수의 갯수 만큼 나눔 (int를 쓴 이유는 소수점이 나오는걸 방지하기 위해)

# --------------------------------------------
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드를 리스트 내포 이용하여 구현 (난이도 상)
# 리스트 [1,2,3,4,5]
data=[1,2,3,4,5] # 리스트(대이터)
print([i*2 for i in data if i % 2 == 1 ]) # data만큼 for를 반복 (i에 data대입) 만약 i를 2로 나누어서 나머지가 1인경우 i에 2를 곱하여 저장

