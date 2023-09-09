# # import random
# # # # 반복구문을 중간에 빠저나오는 코드 = break
# # # # break를 만나면 반복이 중단됨
# # # 커피 = 10
# # # 돈 = 300
# # # while 돈:
# # #     print("커피 주기! 그러고 돈받기!")
# # #     커피  = 커피 -1
# # #     print(f"남은 커피는 {커피}개이다")
# # #     if 커피 <= 0:
# # #         print("커피가 다 떨어졌다 판매 중단 (안녕히 가세요)")
# # #         break
# # # input으로 대이터 (defult str)
# # # 그렇기 때문에 int로 감싸줘야함 ( int로 쓰길 원하면)
# # # print("청부살인 기계에 잘왔다. 독극물을 원하면 돈을 넣어라")
# # print("커피자판기에 잘왔다. 커피를 얻고싶으면 1억을 내놔라")
# # ee = 100000000
# # coffee = 10
# # while True:
# #     money = int(input("돈을 넣어주세요:"))
# #
# #     if money == ee:
# #         print("커피를 줍니다.")
# #         coffee = coffee -1
# #         print("남은 커피는 %d개 입니다." % coffee)
# #
# #     elif money > ee:
# #         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
# #
# #         coffee = coffee -1
# #         print("남은 커피는 %d개 입니다." % coffee)
# #
# #     else:
# #
# #         print("돈을 먹고 튀고  커피를 주지 않습니다.")
# #         print(f"남은 돈은 {ee-money}원 입니다.")
# #         print("남은 커피는 %d개 입니다." % coffee)
# #     if coffee == 0:
# #         print("커피가 다 떨어졌습니다. 판매 중단")
# #         break
# #     if random.choice([1,2,3,4,5,6,7,8,9,10]) == 3:
# #         print("특별 할인!")
# #         print(f"{ee} - > {ee + 100000000}원으로 인하!")
# #         ee = ee + 100000000
# # # 누가 가장 못생겼니?
# # # 1. 너 2. 너 3. 너 4.너
# # # 몆번? 1번
# # # 너가 가장 못생겼다.
# # while문에 처음으로 덜아가는 방법은? continue
# # 프로그래밍을 하다 보면 와일문을 빠저나가지 않고 처음으로 돌아가고 싶을때가 있다.
#
# # while a < 10:
# #     a = a + 1
# #     if a % 2 == 0: # a를 2로 나눈 나머지가 0이면
# #         continue # while문의 처음으로 돌아간다.
# #     print(a)
# #
# # 퀴!즈
# # 0 ~ 20사이의 있는 숫자중 짝수만 출력
# a = 0
#
# while a < 21:
#     a = a + 1
#
#     if a % 2 == 1: # a를 2로 나눈 나머지가 0이면
#         continue # while문의 처음으로 돌아간다.
#     print(a)
# # for door
# # for문은 while문과 비슷한 반복문이다.
list = [1,2,3,4,5]
for i in list:
    print(i)

    # 정 - 수 리스트
점수리스트 = [90, 25, 67, 45, 80]
번호 = 0


for 점수 in 점수리스트:
    번호 = 번호 + 1
    if 점수 > 60:
        print(f"{번호}번 학생은 합격입니다.")
    else:
        print(f"{번호}번 학생은 불합격입니다.")


