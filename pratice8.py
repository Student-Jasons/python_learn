# # # # # # 2023-08-05
# # # # # # 자료형의 값을 저장하는 공간
# # # # # import random
# # # # #
# # # # # a = 1
# # # # # # a와 1 이 같다는 의미가 아닌 a라는 변수에 1이라는 값을 대입한다는 의미
# # # # # # 정수가 저자이 되었기 때문에 정수형 변수이다
# # # # # b = '파이썬' # 문자열이 저장된 변수
# # # # # c = [1,2,3] # 리스트가 저장된 변수
# # # # # print(a, b,c )
# # # # # g = a
# # # # # print(g)
# # # #
# # # a = [5,2,3]
# # # # print(a)
# # # # print(a[0])
# # # # print(a[1])
# # # # b = a[2]
# # # # print(b)
# # # # a[0] = 1
# # # # print(a)
# # # from copy import copy
# # # c = copy(a)
# # # print(c)
# # # d =a
# # # print(a is d)
# # a,b = ('사과', '딸기') # a와 b에 각각 저장
# # print(a)
# # print(b)
# # [c,d] = ["파이썬", "왜불러"]
# # print(c)
# # print(d)
# # print(type(a))
# # print(type(d))
# # a,b = b,a # 바꿔
# # print(a)
# # print(b)
#
# # 퀴즈시간
# # 블핑의 과목별 점수는 다음과 같다
# # 과목   점수
# # 국어   80
# # 수학   75
# # 영어   55
# # 블핑의 평균점수를 구하시오
#
# 과목 = [80, 75, 55]
# imsi = 과목[0] + 과목[1] + 과목[2]
# print(imsi/len(과목))
# 퀴즈2
# 서울사는 홍길동씨 주민번호는 881120-1068234이다
# 홍길동씨의 주민번호를 연월일 부분과 그 뒤의 숫자 부분으로 나누어 출력하시오
주민번호 = "881120-1068234"
print(f"19{주민번호[0:2]}년 {주민번호[2:4]}월 {주민번호[4:6]}일" )
print(주민번호[7:14])
# 퀴즈3
a = [1,3,5,4,2]
# 이것을 1,2,3,4,5 리스트형과 5,4,3,2,1 리스트형으로 바꾸시오
a.sort()
print(a)
a.reverse()
print(a)

# 코드주소 : https://github.com/Student-Jasons/python_learn
# 코드주소 : https://url.kr/zkwfyj
