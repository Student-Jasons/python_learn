# 반복문...while
# 조건 반복문
# 조건이 맞는 동안만 반복을 한다.
# a = 0
# while a == 0:
#     print("홍길동")

treehit = 0
while treehit < 10:   # treehit 가 10 보다 작을동안.
    treehit = treehit + 1   # treehit를 +1 씩 증가시켜라.
    print("나무를 %d 번 찍었습니다" % treehit)   # %d = 정수변수를 치환할때 % treehit = % 는 treehit (정수)를 집어넣어라.
    if treehit == 10:   # 만약 treehit 가 10 이라면
        print("나무가 넘어갑니다.")
        
# 여러가지 성택지 중 하나를 선택해서 입력받는 예재를 만들어 보자.
prompt = """
... 1,Add
... 2,Del
... 3,List
... 4,Quit
...""" 
# """ = 줄을 내러서 씀

number = 0
숫자 = 0
while number != 4:   # number 라는 변수가 4가 아닐때
    print(prompt)
    number = int(input("입력번호:"))   # 사용자로부터 입력을 받기까지 대기. ***
    if number == 4:   # 4 : quit (종료) 만약 사용자가 입력한 숫자가 4 이면 종료한다.
        print("종료")
    if number == 1:   # 사용자가 선택한 정수가 1 일때
        print("1번 : add 선택")
        더하기 = int(input("더할 숫자 입력해주세요."))
        숫자 = 숫자 + 더하기   # 사용자가 입력한 정수를 숫자에 저장한다.
    if number == 3:
        print("3번 : List 선택")
        print("현재 저장 되어 있는 수는 %d 입니다" % 숫자)   # 기존에 더한 정수를 더해 보여준다. ***
        print("다음 변수 입력")
    if number == 2:
        print("삭제 선택 (저장되에 있는 수 = 0)")   # 저장된 변수를 지운다.
        숫자 = 0