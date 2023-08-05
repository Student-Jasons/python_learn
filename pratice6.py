import random
import time


# while True:
#     a = random.choice(["황준섭", "동아형"])
#     b = random.choice(["잘생김", "못생김", "예쁨", "돼지", "마약쟁이", "원빈급 외모"])
#     print(f'{a}은 {b}')
#     # if a == "황준섭" and b == "잘생김":
#     #     print("인정")
#     # if a == "동아형" and b == "잘생김":
#     #     print("인정안함")
#     # if a == "동아형" and b == "못생김":
#     #     print("인정함")
#     time.sleep(0.1)
#     break
# 딕서너리에서 key값을 사용해 value 값 얻기
# 점수 = {'국어' : 80, '수학' : 99}
# print(점수["국어"]) # 점수 변수의 국어 key값에서 80 value 변환
# print(점수["수학"])
def 딕셔너리전체평균자동계산프로그램(dic):
    im = 0
    for i in dic:
        im = im + dic[i]
    return im / len(dic)
def 총점수구하기(dic):
    im = 0
    for i in dic:
        im = im + dic[i]
    return im
# print(f'총점수 = {점수["국어"] + 점수["수학"] }')
# print(f"평균 = {(점수['국어'] + 점수['수학']) / len(점수)}")
# 총점수 = 점수["국어"] + 점수["수학"]
# 평균 = 딕셔너리전체평균자동계산프로그램(점수)
# print(f"총점수 : {총점수}, 평균 : {평균}")
과목 = {"국어" : 80,"수학" : 1000,"영어" : 4234,"과학" : 52345, "체육" : 80, }
print(f"총점수 : {총점수구하기(과목)}, 평균 : {딕셔너리전체평균자동계산프로그램(과목)}")

주소록 = {"이름": "홍길동", "전번" : "01055559999", "생일": "20230715"}
apple = {"이름" : "팀 쿡", "전화번호" : "https://support.apple.com/ko-kr/HT201232", "생일" : "19601101"}
print(f'팀쿸님 전화번호(고객선터)는 {apple["전화번호"]} 입니다')
# name = input("이름내놔")
# birtudat = input("생일")
# ohibebynber = input("전번")
# 황준섭 = {"이름" : name, "생일" : birtudat, "전번" : ohibebynber}
# print(f"황준섭의 생일은 {황준섭['생일']} 입니다")
# print(황준섭.keys())
# 홍길동키값 = list(황준섭.keys())
# print(홍길동키값)
print(apple.values())
apple팀쿸정보 = list(apple.values())
print(apple팀쿸정보)

print(apple.items())
자료 = list(apple.items())
print(자료)
# 생일 반환
print(자료[2][1])

print(f"{자료[2][1][0:4]}년 {자료[2][1][4:6]}월 {자료[2][1][6:]}일")
print()

# 해당 key가 딕셔너리 안에 있는지 조사하기
a = {'name' : '4444', 'phone' : "+1 (666) 666-6666", 'birth':'4444-04-04', 'email' : '4444@6666.death'}
print('name' in a)
print('email' in a)
