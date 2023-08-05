# # # 집합 자료형
# # # 집합은 2.3부터 지원
# # # 집합에 관련된 것을 쉽게 처리하기 위해 만든거
# #
# # sl = set([1,2,3])
# # print(sl)
# # print(type(sl))
# # s2 = set()
# # print(s2)
# #
# # # s3 = set('निहाओ')
# # s3 = set('hello') #중복을 허용 x
# #
# # print(s3)
# # t1 = tuple(sl) # 튜플 자료향으로 변환시켜 t1에 저장
# # print(type(t1))
# #
# # l1 = list(t1) # 리스트 자료용으로 젼환해서 l1에 저장
# # print(l1)
# # print(type(l1))
# # set 자료형의 교집항,합집합,차집합 구하기
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# print(s1 & s2) # 중복되는 요소를 반환해줌
# print(s1.intersection(s2)) # 위와 같은 기능
# # 합집합
# print(s1 | s2) # 중복되는 요소를 하나로 처리후 반환
# print(s1.union(s2)) # |은 앤터키 위에 있는거.
# # 차집합
# print(s1 - s2) # s1에서 s2에 있는 요소를 제거후 반환
# print(s1.difference(s2))
# print(s2 - s1) # s2에서 s1에 있는 요소를 제거후 반환
#
# ss1 = set([1,2,3])
# ss1.add(4) # add는 집합에 요소를 추가하는 함수
# print(ss1)
#
# ss1.update([5,6,7]) #여러가지 추가할때 유용
# # print(ss1)
# # # 특정값 지울떄
# # ss1.remove(4)
# # print(ss1)
# # # 불(bool) 자료형
# # # 참과 거짓을 나타내는 자료형
# a = True
# b = False
# print(type(a))
# print(type(b))
# # bool =X fire
# print(1==1)
# print(1==2)
# print(1>2)
# print(1<2)
# a = 5
# b = 3
# print(a>b)
# print(a<b)
# 불에 내장함수
print(bool('python')) # 빈문자열이 아님으로 True
print(bool('')) # 빈문자열이므로 False
print(bool('2'))
print(bool(4)) # 0이 아닌 숫자는 참
print(bool(0)) # 0은 거짓
print(bool([1,2,3]))  # 요소가 있으므로 True
print(bool([])) # 요소가 없으므로 False
import os
