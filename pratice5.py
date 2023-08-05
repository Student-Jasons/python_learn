# pratice5.py
# 리스트의 요소 삽입
a = [1,2,3]
a.insert(0,4) #a[0] 자리의 4삽입
print(a)
a.sort(
) # a 리스트 정렬
a.reverse()
print(a)
a.insert(1,1.5)
print(a)
# 리스트의 삭제
b = [4,5,6,4,5,6]
# del b[1] #특정 자리의 삭제
print(b)
b.remove(5)      # 리스트의 자료중 첫번째껏만 삭제됨 ㅋ
b.remove(5)      # 리스트의 자료중 첫번째껏만 삭제됨 ㅋ

print(b)
# 리스트의 끄어내기 pop
a = [1,2,3,2,4,3,5,6]
a.pop() #마지막꺼 끌어내고 삭제
print(a)
a.pop(1)
print(a)
print(a.pop(1)) # a 리스트중 2번째 요소를 끌어내 반환
print()

# 리스트의 요소 카운트 세기
c = [4,5,6,4,4,4,1]
print(a.count(4))
print('위 대이터에는4가',c.count(4),'개 포함되어잇다')

# 리스트의 확장

a = [1,2,3]
b = [7,8,9]

a.extend([4,5,6]) # 리스트 자료형식으로 더해줄때
# a.append([4,5,6])
print(a)
print(a+b)

# tuple
# 리스트는 대괄호 튜플을 ()
# 리스트는 생성,수정, 삭제 ok
# 튜플 no
# 튜플...................................... 자료형은 요소가 하나일때 ,로 끝내야함
t1 = (1,2,'사과', '배')
print(type(t1))
# 튜플의 인!댁!싱

print(t1[2])
print(t1[2:])
# 튜플의 연산
# 튜플의 연산
t2 = (3,4)
print(t2)
print(t2 *3)
print(t1 + t2)
print(len(t2))

# 오퀴

# (1,2,3)이라는 튜플에 4를 추가하여 (1,2,3,4)로 만들어 출력해보자
q1 = (1,2,3)
q2 = (4,)
print(q1+q2)
# a
a = (1,2,3)
print(a + (4,5,6))

# finnal 지려향
# 리스트형, 튜플형, 딕sasasu
# 딕셔너리 자료형의 형태는 {key:value} 형태로 저장
dic = {}
dic["key"] = "value"
print(dic)
a = {1 : 'hi'}
b = {"샤과" : [1,2,3]}
print(a)
print(b)
# 딕셔너리의 추가,삭제
a[2] = 'bye' #key = 2 value = bye인거 추가
print(a)
a[5] = '앤녕'
print(a)
a["4번째"] = "잘가"
# a["동아형"] = "잫ㄹ생김"

print(a)
del a[1] #key값이 1인 용소 항목으로 몽땅 삭제
# 동아형 너무 wkftodrla 너무 cjswpdla rjqsk cjswpdla sork qhs tkfkawnddp wpdlf whgdmsemt fd zz
print(a)
# 딕셔너리의 사용
직업 = {"kim yona" : "스케이트","손흥민":"축구", "나는" : "파이썬", "동아형":"tptkddptj rkwkd ajtwls qnslasladprptj xodjsks tlsehdrkxdms djqcjdsks cjswo tlsehd"}

# wkwnwktn tkdydz

황준섭 잘생김
황준섭 잘생김
황준섭 잘생김