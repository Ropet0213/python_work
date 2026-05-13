#=======================================================================
# 파일명 : ch08_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-05-13
#=======================================================================

#항상 넣는 코드들 (화면 초기화, 시각적 너비 계산, 시각적 정렬)
import os
import subprocess

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def get_vis_width(text):
    width = 0
    for char in text:
        if ord('가') <= ord(char) <= ord('힣'):
            width += 2
        else:
            width += 1
    return width

def vis_center(text, total_width):
    current = get_vis_width(text)
    padding = (total_width - current) // 2
    return " " * padding + text + " " * (total_width - current - padding)

def vis_ljust(text, total_width):
    current = get_vis_width(text)
    return text + " " * (total_width - current)

def vis_rjust(text, total_width):
    current = get_vis_width(text)
    return " " * (total_width - current) + text

# 메인 출력 UI
WIDTH = 60 #상자 너비 (되도록 변경 ㄴㄴㄴㄴㄴ)

clear_screen()

border = "─" * (WIDTH - 2)

print("┌" + border + "┐")
print("│" + vis_center("프로그램 목록", WIDTH - 2) + "│")
print("├" + border + "┤")
print("│" + vis_ljust("  1. ch08_func_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  2. ch08_func_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  3. ch08_func_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  4. ch08_type_a1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  5. ch08_type_a2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  6. ch08_type_b1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  7. ch08_type_b2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  8. ch08_type_c2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  9. ch08_type_d1.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 10. ch08_type_d2.py", WIDTH - 2) + "│")
print("└" + border + "┘")
print()

selected_program = int(input("실행할 프로그램 번호를 입력하세요: "))

#ch08_func_1.py
if selected_program == 1:
    def  sum (num1, num2) :
        add = num1 + num2
        return add
    ##메인프로그램 소스코드
    result = sum (10, 20)
    print(result)

# ch08_func_2.py
if selected_program == 2:
    #파이썬으로 다시 쓴 동일구조 (C 예시→ Python)
    def  sum (a, b) :            # ← 형식 매개변수(a, b)
        c = a + b
        return c
    #메인 부분
    num1 = 2
    num2 = 5
    total = sum (num1, num2)     # ← 실 매개변수(num1, num2)
    print(total)

# ch08_func_3.py
if selected_program == 3:
    #사용자 정의 함수 소스코드
    def  sum (num1, num2) :      # ← (num1, num2) : 형식 매개변수
        add = num1 + num2
        return add
    #메인 프로그램 소스코드
    result = sum (10, 20)        # ← (10, 20) : 실 매개변수
    print(result)

# ch08_type_a1.py
if selected_program == 4: 
    #A타입 함수 정의와 호출
    def  a_type() :
        print(">> A타입의 함수 정의 방법입니다.")
    #호출
    a_type()

# ch08_type_a2.py
if selected_program == 5:
    # A타입의 사용자 정의 함수 소스코드 (시작부분)
    def  a_type() :
        print(">> 시작: 사용자 정의 함수- A 타입")
        number = """
        1. 컬링
        2. 피겨스케이팅
        3. 알파인스키
        4. 봅슬레이
        5. 쇼트트랙
        6. 그냥종료
        """
        print(number)

        print(">> 종료: 사용자 정의 함수- A 타입")
        print("-" * 38)
#메인 프로그램 소스코드
    print("=" * 55)
    print("■ A타입의 사용자 정의 함수 프로그램")
    print("-" * 55)
    print(">> 사용자 정의 함수를 호출합니다...")
    print("-" * 38)
    a_type ( )
    print(">> 메인 프로그램을 종료합니다.")
    print("=" * 55)

# ch08_type_b1.py
if selected_program == 6:
    # B 타입함수정의와호출
    def  b_type (num1, num2) :
        add = num1 + num2
        print(f">> B 타입 함수 호출 결과: {add}")
    # 호출
    b_type (10, 20)

# ch08_type_b2.py
if selected_program == 7:
# B 타입의 사용자 정의 함수 소스코드 (시작부분)
    def  b_type (choiceValue) :
        print("-" * 38)
        print("\n>> 시작: 사용자 정의 함수-B 타입\n")
        number = { 1: '컬링',
        2: '피겨스케이팅',
        3: '알파인스키',
        4: '봅슬레이',
        5: '쇼트트랙',
        6: '선택안함' }
        if choiceValue == 1 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        elif choiceValue == 2 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        elif choiceValue == 3 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        elif choiceValue == 4 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        elif choiceValue == 5 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        elif choiceValue == 6 :
            print(">> 종목: [ ", end='')
            print(number.get(choiceValue) + " ] \n")
        else :
            print(">> 유효 숫자 입력 오류!! \n")
            print(">> 종료: 사용자 정의함수-B 타입\n")
            print("-" * 38)
    print("=" * 55)
    print("■ B 타입의 사용자 정의 함수 프로그램")
    print("-" * 55)
    print(">> 선택할 종목은 다음과 같습니다.")
    number = """
    1. 컬링
    2. 피겨스케이팅
    3. 알파인스키
    4. 봅슬레이
    5. 쇼트트랙
    6. 그냥종료
    """
    print(number)
    print("-" * 55)
    sports = int(input(">> 종목 선택(1~6) : "))
    print("-" * 55)
    print(">> 사용자 정의 함수를 호출합니다...")
    b_type (sports)


# ch08_type_c2.py
if selected_program == 8:
    trivia = {
        1: '컬링은 16세기 스코틀랜드에서 가정용 빗자루로 시작된 스포츠입니다.',
        2: '피겨스케이팅은 동계 스포츠중에서 가장 오래된 역사를 가지고 있습니다.',
        3: '알파인스키는 모터를 사용하지 않는 스포츠중에서 가장 빠른 속력을 자랑합니다.',
        4: '봅슬레이는 초반에 속력을 내기 위해서 머리를 흔드는 것(bobbing)에서 유래했습니다.',
        5: '쇼트트랙은 대한민국이 압도적인 성적을 내고 있는 종목입니다.',
        6: None
    }

    def c_type():
        print("-" * 38)
        print("\n>> 시작: 사용자 정의 함수- C 타입\n")
        number = {
            1: '컬링',
            2: '피겨스케이팅',
            3: '알파인스키',
            4: '봅슬레이',
            5: '쇼트트랙',
            6: '선택안함'
        }
        choiceValue = int(input(">> 선택(1~6) : "))
        print("")
        if 1 <= choiceValue <= 6:
            return number.get(choiceValue), trivia.get(choiceValue)
        else:
            return " 유효 숫자 입력 오류!! ", None

    ## 메인프로그램소스코드
    print("=" * 55)
    print("■ C 타입의 사용자 정의 함수 프로그램")
    print("-" * 55)
    print(">> 선택할 종목은 다음과 같습니다.")
    number = """
    1. 컬링
    2. 피겨스케이팅
    3. 알파인스키
    4. 봅슬레이
    5. 쇼트트랙
    6. 그냥종료
    """
    print(number)
    print("-" * 55)
    print(">> 사용자 정의 함수를 호출합니다...")
    value, fact = c_type()
    print(f">> 종목: [ {value}] \n")
    if fact:
        print(f">> 그거 아세요? : {fact}\n")
    print("-" * 55)
    print(">> 메인 프로그램을 종료합니다.")
    print("=" * 55)

# ch08_type_d1.py
if selected_program == 9:
    # D 타입 함수 정의와 호출
    def  d_type (num1, num2) :
        add = num1 + num2
        return add
    # 호출
    result = d_type (10, 20)
    print(result)

# ch08_type_d2.py
if selected_program == 10:
    # D 타입의 사용자 정의 함수 소스코드 (시작부분)
    def  d_type (choiceValue) :
        print("-" * 38)
        print("\n>> 시작: 사용자 정의 함수- D 타입\n")
        number = { 1: '컬링',
        2: '피겨스케이팅',
        3: '알파인스키',
        4: '봅슬레이',
        5: '쇼트트랙',
        6: '선택안함' }
        if choiceValue == 1 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        elif choiceValue == 2 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        elif choiceValue == 3 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        elif choiceValue == 4 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        elif choiceValue == 5 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        elif choiceValue == 6 :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            print(">> 종료: 사용자 정의 함수- D 타입\n")
            return (number.get(choiceValue))
        else :
            print(f">> 메인에서 입력한 값: {choiceValue} \n")
            return " 유효숫자 입력 오류!! "
    ## 메인프로그램 소스코드
    print("=" * 55)
    print("■ D 타입의 사용자 정의 함수 프로그램")
    print("-" * 55)
    print(">> 선택할 종목은 다음과 같습니다.")
    number = """
1. 컬링
2. 피겨스케이팅
3. 알파인스키
4. 봅슬레이
5. 쇼트트랙
6. 그냥종료
"""
    print(number)
    print("-" * 55)
    su = int(input(">> 선택(1~6) : "))
    print("-" * 55)
    print(">> 사용자 정의 함수를 호출합니다...")
    value = d_type (su)
    print(f">> 종목: [ {value}] \n")
    print("-" * 55)
    print(">> 메인 프로그램을 종료합니다.")
    print("=" * 55)
