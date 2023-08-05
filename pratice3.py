# # f 문자열 포메팅
hansomeguy = "황준섭"
print(f"{hansomeguy}은 잘생겻다")
print(f"{hansomeguy}은 천제다")
#
# 이름 = '홍길동'
# 나이 = 21
# print(f"나의 이름은 {hansomeguy}입니다 나이는 {나이}입니다.")
# # 정렬방법
# # 넵
# print(f'{"안녕":*<10}') # 왼정렬
# print(f'{"바이":=>10}') # 오정렬
# print(f'{"하이":-^10}') # 가정렬
#
# 문자열 관련 함수

# a="habby"
# print(a.count('b'))
# b = 'Python is the best choice'
#
# print(b.count('t'))
# print(b.find('b')) # b 변수에서 b의 슬라이싱 의치 반환
# print(b.find('z')) # 없으면 -1 반환
# print(b.index('P')) # find = index
# print(b.count('c'))
#
# # 문자열 sapip
#
# 문자 = 'ganadaramanasa'
# print(",".join('ganadarasa'))
# print("!".join(문자)) #문자열 사이의 콤마넣기 쌉ganen
# 문지2 = ".".join('ganadarasa') # 변수에도 저장가능
# print(문지2)
# print("!".join(문지2)) # 문자와 문자 사이의 삽입

# 소문자를 -> 대문자, 대문자 -> 소문자
# a = 'hi'
# b = "HI"
# print(a.upper())
# print(b.lower())
# print(b.upper())
#
# print(a)
#
# # 여백 지우기
#
# c = '    안녕                '
# print(c)
# print(c.lstrip()) # 왼쪽 야벡을 지우고 출력
# print(c.rsplit()) # 오른쪽 여백을 지우고 추력
# print(c.strip()) #여백을 지우고 출력 !!! B = boss !!!

# 문자열 바꾸기

단문 = '나는 내가 너무 좋아!! 하하하'
print(단문.replace('내', "황준섭")) # 문자ㄹ열을 리플레이스 한다 ( 예 내를 황준섭으로)
# 실제로 바뀌는게 아님! ^
#                    |
# 겁나 짱짱 중여한거

# 리스트
# list = []
# # 리스트는 한 뱐수의 다양한걸 넣는거
# 리스트 = [1,3,5,7,9] # 데괄호화, 표로 구분지어서 여러 자료들로 바꿈
# a = [] #변수를 자려향ㅇ,로
# b = 0
# print(type(a))
# print(type(b))
# print(type(단문))
# print(리스트)

# 리스트의 인댁싱과 슬라이싱
a = [1,2,4,5,7,8]
print(a[3]) # a리스트에서 4번째자료 반환
print(a[1]+a[4]) # 자료형에서 자료를 가져와서 연산도 가능
print(a[-1]) #뒤에서 첫번째 반환
b = ['사괴', '딸기', '바나나', ['거봉', '샤인머스켓', '황금달기']]

# b 리스트 자료형에서 4번쨰의서 3번째 반환

print(b)
print(b[3])
print(b[3][2])
