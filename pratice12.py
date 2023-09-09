# # # # 2023 09 02일
# # # # for문과 함깨 자주사용하는 range 함수
# # # # a = range(10)
# # # # print(a)
# # # # print(type(a))
# # # # for i in range(10):
# # # #     print(i)
# # # # add = 0
# # # # for i in range(1,11):
# # # #     add = add + i
# # # #     print(add)
# # # # print(add)
# # # # # 위는 1+2+3+4+5+6+7+8+9+10
# # # # # = 55
# # # # marks = [90,25,67,45,80]
# # # # for number in range(len(marks)):
# # # #     if marks[number] < 60:
# # # #         continue
# # # #     print(f"{number+1}번 학생 축하합니다. 합격입니다.")
# # # a = "hellow"
# # # marks = [90,25,67,45,80]
# # # for number in range(len(marks)): # marks의 개수가 5임으로 0-4까지 범위 (중요)
# # #     if marks[number] < 60: # number값은 0-4까지 범위
# # #         continue # 중요
# # #     print("%d번 학생 축하합니다. 합격입니다." %(number+1))
# # # # 퀴즈
# # # # for문과 range함수만을 사용하여 1부터 100까지 더해보시오
# # # imsi = 0
# # # for i in range(1, 101):
# # #     imsi = imsi + i
# # #     print(imsi)
# # # # print(imsi)
# # # 구구단 2에서 9단까지
# # for i in range(2,10): # 2-9까지 반복
# #     print(f"{i}단 ", end= "")
# #     for j in range(1, 10):# 1-9까지 반복
# #         print(i * j, end= " ") # 2-9 X 1-9             이런식으로 출력
# #     print('') #\n 대용
# #     # 여기서 print(i * j, end= " ")와 같이 end를 넣어준 이유는 해당 결과값을 출력할때
# #     # 다음줄로 넘기지 않고 그줄에 계속해서 출력하기 위해서이다.
# #     # 그다음에 print('')는 2단 3단들을 구분하기 위해 2번쨰 for문이 끝나면 다움줄
# #     # 부터 출력하게 해주는 문장이다.
#
#
#
#
# # 2023-09-09
# # 리스트 내포 사용하기.
# # 리스트 안에 for문을 포함하는 리스트 내포를 이용하면. 좀더 편리하고.  직관적인 프로그램을 만들수 있다.
# # a = [1,2,3,4]
# # result = []
# # for num in a: # a에 항목이 4개 있음으로 4번 반복
# #     result.append(num * 3) # 3, 6, 9, 12가 저장이 될것, 3배를 하기 때문에.
# #     print(result)
# # print(result)
#
# # a = [1,2,3,4]
# # result = [num*3 for num in a]
# # # for num in a:
# # #     result.append(num * 3)
# # # 라는 문장을 한 문장으로 단축하여 리스트에 넣은것.
# # print(result) # [3, 6, 9, 12]
# # 퀴즈 : [1,2,3,4]중에서 짝수에만 3을 곱하여 담아보자... 결과출력
# data = [1,2,3,4]
# result = []
# for i in data:
#     if i % 2 == 0: # 만약 i를 2로 나눈 나머지가 2라면
#         result.append(i*3) # i를 3으로 곱하여 추가
#     else:#아니라면
#         result.append(i) #원본 추가
#
# print(result)
# #리스트 내포 버전
# result = [num * 3  for num in data if num %2 == 0 ]#append와 :빼고 전부 들어감
# # 앞에서 뒤로 :과 append뻬고 넣음
# print(result)
# #
# 퀴-즈 2
# 구구단의 모든 값을 리스트에 담아 보자.
result = [i*j for i in range(2, 10) for j in range(1,10)] # 구구단 내포버전
# 내포의 append는 1회밖에 사용불가
result2 = []
for i in range(2,10): # 2-9까지 반복
    for y in range(1,10):
        result2.append(i*y)
#일반버전
print(result) # 내포
print(result2) # 일반
# apple 사랑해요
