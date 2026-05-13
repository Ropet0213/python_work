#=======================================================================
# 파일명 : ch08_test_02.py
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
print("│" + vis_ljust("   1. ch08_01_1.py    2. ch08_01_2.py    3. ch08_01_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("   4. ch08_02_2.py    5. ch08_02_3.py    6. ch08_03_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("   7. ch08_03_2.py    8. ch08_03_3.py    9. ch08_03_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  10. ch08_04_1.py   11. ch08_04_2.py   12. ch08_04_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  13. ch08_04_4.py   14. ch08_05_1.py   15. ch08_05_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  16. ch08_05_3.py   17. ch08_06_1.py   18. ch08_06_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  19. ch08_06_3.py   20. ch08_06_4.py   21. ch08_06_5.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  22. ch08_07_1~2.py 23. ch08_07_3.py   24. ch08_08_1.py", WIDTH - 2) + "│")
print("└" + border + "┘")
print()

selected_program = int(input("실행할 프로그램 번호를 입력하세요: "))

#ch08_01_1.py
if selected_program == 1:
    #학생이 30명이면 이 블록을 30번 반복해야함
    score1 = 85
    if score1 >= 90:
        grade1 = 'A'
    elif score1 >= 80:
        grade1 = 'B'
    elif score1 >= 70:
        grade1 = 'C'
    else:
        grade1 = 'F'
    print(f'학생1: {score1}점→ {grade1}')

#ch08_01_2.py
if selected_program == 2:
    def get_grade(score): # 한번만 작성
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'
    #몇 명이든 한줄!
    print(f'학생1: {get_grade(85)}')
    print(f'학생2: {get_grade(72)}')
    print(f'학생3: {get_grade(95)}')

#ch08_01_3.py
if selected_program == 3:
    def say_hello():
        print('안녕하세요!')
    say_hello()
    say_hello()

#ch08_02_2.py
if selected_program == 4:
    def greet_person(name): # name은 매개변수
        print(f'안녕하세요, {name}님!')
    greet_person('김철수') # '김철수'는 인수
    greet_person('이영희')

#ch08_02_3.py
if selected_program == 5:
    def introduce(name, age):
        print(f'저는{name}이고, {age}살입니다.')
    introduce('박민준', 20)
    introduce('최수아', 22)

#ch08_03_1.py
if selected_program == 6:
    def greet(name, greeting='안녕하세요'): # greeting에 기본값
        print(f'{greeting}, {name}님!')
    greet('김철수')              # greeting 생략→ 기본값 사용
    greet('이영희', '반갑습니다')  # greeting 직접 지정

#ch08_03_2.py
if selected_program == 7:
    def make_coffee(type, size, sugar=0):
        print(f'{size} {type}, 설탕{sugar}개')
    make_coffee('아메리카노', 'large', 2)     # 위치 인수
    make_coffee(size='medium', type='라떼')   # 키워드 인수

#ch08_03_3.py
if selected_program == 8:
    def sum_all(*numbers):   # *numbers → 튜플로 받음
        total = 0
        for n in numbers:
            total += n
        return total
    print(sum_all(1, 2, 3))        # → 6
    print(sum_all(10, 20, 30, 40)) # → 100

if selected_program == 9:
    def power(base, exp=2):
        return base ** exp
    print(power(3))           # → 9 (기본값exp=2)
    print(power(2, 10))       # → 1024
    print(power(exp=3, base=5)) # 키워드 인수 → 125

#ch08_04_1.py
if selected_program == 10:
    def add(a, b):
        result = a + b
        return result  # 결과를 돌려줌
    total = add(3, 5)  # 반환값을 변수에 저장
    print(total)       # → 8
    print(add(10, 20)) # → 30 (바로 출력도 가능)

#ch08_04_2.py
if selected_program == 11:
    def say_hi():
        print('Hi!')  # 출력만 하고 반환값 없음
        return None
    result = say_hi()  # None이 반환됨
    print(result)      # → None

#ch08_04_3.py
if selected_program == 12:
    def safe_divide(a, b):
        if b == 0:    # 0으로 나눌수 없으면
            return None  # 즉시 종료
        return a / b     # 나눗셈 결과 반환
    print(safe_divide(10, 2)) # → 5.0
    print(safe_divide(10, 0)) # → None

#ch08_04_4.py
if selected_program == 13:
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32
    print(celsius_to_fahrenheit(0))   # → 32.0
    print(celsius_to_fahrenheit(100)) # → 212.0
    print(celsius_to_fahrenheit(37))  # → 98.6 (체온)

#ch08_05_1.py
if selected_program == 14:
    def min_max(numbers):
        return min(numbers), max(numbers)  # 두값 반환
    result = min_max([3, 1, 4, 1, 5, 9, 2])
    print(result) # → (1, 9) 튜플로 반환
    # 언패킹으로 받기 (권장!)
    low, high = min_max([3, 1, 4, 1, 5, 9, 2])
    print(f'최솟값: {low}, 최댓값: {high}')

#ch08_05_2.py
if selected_program == 15:
    def stats(numbers):
        total   = sum(numbers)
        average = total / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        return total, average, minimum, maximum
    scores = [85, 92, 78, 96, 67]
    t, avg, lo, hi = stats(scores)
    print(f'합계:{t}, 평균:{avg:.1f}, 최저:{lo}, 최고:{hi}')

#ch08_05_3.py
if selected_program == 16:
    def swap(a, b):   # 두값을 바꿔서 반환
        return b, a
    x, y = 10, 20
    x, y = swap(x, y)
    print(x, y)       # → 20 10
    # 응용: 원의넓이와 둘레 동시 계산
    import math
    def circle(r):
        return math.pi*r**2, 2*math.pi*r
    area, perimeter = circle(5)
    print(f'넓이:{area:.2f}, 둘레:{perimeter:.2f}')

#ch08_06_1.py
if selected_program == 17:
    # 지역변수: 함수 안에서만 존재
    def my_func():
        local_var = '나는 지역변수!'
        print(local_var)
    my_func()         # → 지역 변수
    # print(local_var) → NameError!

#ch08_06_2.py
if selected_program == 18:
    # 전역변수: 어디서나 읽기 가능
    global_var = '나는 전역변수!'
    def my_func():
        print(global_var)  # 읽기는 가능!
    my_func()   # → 나는 전역변수!
    print(global_var) # → 나는 전역변수!


#ch08_06_3.py
if selected_program == 19:
    def my_func():
        local_var = '나는 지역변수!' # 함수안에서만 존재
        print(local_var)
    my_func()        # → 나는 지역변수!
    #print(local_var) # 오류! 함수 밖에서는 접근  불가

#ch08_06_4.py
if selected_program == 20:
    count = 0  # 전역변수
    def increase():
        global count  # 전역 변수임을 선언
        count += 1
    increase()
    increase()
    print(count)  # → 2

#ch08_06_5.py
if selected_program == 21:
    x = 10
    def test():
        x = 20  # 이건 지역변수!
        print('함수안:', x)
    test()
    print('함수밖:', x)  # x = 10 (전역변수)

#ch08_07_1~2.py
if selected_program == 22:
    #함수 분리 전과 후의 코드 예시를 만들어봄
    def print_two_boxes():
        border = "─" * (WIDTH - 2)

        left_lines = [
            "ch08_07_1.py",
            "",
            "# 함수 분리 전 ← 뒤죽박죽",
            "name = input('이름: ')",
            "score = int(input('점수: '))",
            "if score >= 90: grade = 'A'",
            "elif score >= 80: grade = 'B'",
            "else: grade = 'C'",
            "print(f'{name}: {grade}')",
        ]

        right_lines = [
            "ch08_07_2.py",
            "",
            "def get_input():",
            "    name = input('이름: ')",
            "    score = int(input('점수: '))",
            "    return name, score",
            "def get_grade(score):",
            "    if score >= 90: return 'A'",
            "    elif score >= 80: return 'B'",
            "    else: return 'C'",
            "def print_result(name, grade):",
            "    print(f'{name}님의 등급: {grade}')",
            "def main(): # 전체 흐름 관리",
            "    name, score = get_input()",
            "    grade = get_grade(score)",
            "    print_result(name, grade)",
            "main() # 프로그램 시작",
        ]

        #두 상자에 들어가게 줄맞추기
        max_lines = max(len(left_lines), len(right_lines))
        left_lines  += [""] * (max_lines - len(left_lines))
        right_lines += [""] * (max_lines - len(right_lines))    

        #상자 그리기
        print("┌" + border + "┐" + " " + "┌" + border + "┐")
        print("│" + vis_center("함수 분리 전 코드 예시", WIDTH - 2) + "│" + " " +
              "│" + vis_center("함수 분리 후 코드 예시", WIDTH - 2) + "│")
        print("├" + border + "┤" + " " + "├" + border + "┤")
        for l, r in zip(left_lines, right_lines):
            print("│" + vis_ljust(" " + l, WIDTH - 2) + "│" + " " +
                  "│" + vis_ljust(" " + r, WIDTH - 2) + "│")
        print("└" + border + "┘" + " " + "└" + border + "┘")

    #메인 프로그램 소스코드
    print_two_boxes()


    print() 
    choice = input("실행할 코드 선택 (1 / 2): ").strip()

    def run_code_1():
        clear_screen()
        print("[ 함수 분리 전 실행 결과 ]")
        print()
        name = input('이름: ')
        score = int(input('점수: '))
        if score >= 90: grade = 'A'
        elif score >= 80: grade = 'B'
        else: grade = 'C'
        print(f'{name}: {grade}')

    def run_code_2():
        clear_screen()
        print("[ 함수 분리 후 실행 결과 ]")
        print()
        def get_input():
            name = input('이름: ')
            score = int(input('점수: '))
            return name, score
        def get_grade(score):
            if score >= 90: return 'A'
            elif score >= 80: return 'B'
            else: return 'C'
        def print_result(name, grade):
            print(f'{name}님의 등급: {grade}')
        def main():
            name, score = get_input()
            grade = get_grade(score)
            print_result(name, grade)
        main()

    if choice == "1":
        run_code_1()
    elif choice == "2":
        run_code_2()
    else:
        print("잘못된 입력입니다.")

#ch08_07_3.py
if selected_program == 23:
    def is_even(n):  # n이 짝수이면 True 반환
        return n % 2 == 0
    def classify_numbers(numbers):
        evens = [n for n in numbers if is_even(n)]
        odds  = [n for n in numbers if not is_even(n)]
        return evens, odds
    e, o = classify_numbers([1,2,3,4,5,6,7,8])
    print('짝수:', e)  # [2, 4, 6, 8]
    print('홀수:', o)  # [1, 3, 5, 7]

#ch08_08_1.py
if selected_program == 24:
    def add(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b
    def divide(a, b):
        if b == 0:
            return None
        return a / b
    def power(a, b=2): return a ** b
    def statistics(numbers):
        total   = sum(numbers)
        average = total / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        return total, average, minimum, maximum

    def show_menu():
        border = "─" * (WIDTH - 2)
        clear_screen()
        print("┌" + border + "┐")
        print("│" + vis_center("나만의 계산기", WIDTH - 2) + "│")
        print("├" + border + "┤")
        print("│" + vis_ljust("  1. 더하기        2. 빼기", WIDTH - 2) + "│")
        print("│" + vis_ljust("  3. 곱하기        4. 나누기", WIDTH - 2) + "│")
        print("│" + vis_ljust("  5. 거듭제곱      6. 통계", WIDTH - 2) + "│")
        print("│" + vis_ljust("  0. 종료", WIDTH - 2) + "│")
        print("└" + border + "┘")

    def calculate(choice):
        if choice in ['1','2','3','4','5']:
            a = float(input('첫 번째 숫자: '))
            b = float(input('두 번째 숫자: '))
            if choice == '1':
                print(f'결과: {add(a, b)}')
            elif choice == '2':
                print(f'결과: {subtract(a, b)}')
            elif choice == '3':
                print(f'결과: {multiply(a, b)}')
            elif choice == '4':
                r = divide(a, b)
                if r is None:
                    print('0으로 나눌 수 없습니다!')
                else:
                    print(f'결과: {r}')
            elif choice == '5':
                print(f'결과: {power(a, b)}')
        elif choice == '6':
            border = "─" * (WIDTH - 2)
            print("┌" + border + "┐")
            print("│" + vis_center("통계 계산", WIDTH - 2) + "│")
            print("├" + border + "┤")
            while True:
                try:
                    raw = input('  숫자 입력 (공백 구분): ')
                    nums = list(map(float, raw.split()))
                    if len(nums) < 2:
                        print('  숫자를 2개 이상 입력해주세요.')
                        continue
                    break
                except ValueError:
                    print('  올바른 숫자를 입력해주세요.')
            t, avg, lo, hi = statistics(nums)
            print("├" + border + "┤")
            print("│" + vis_ljust(f"  개수  : {len(nums)}개", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  합계  : {t:.2f}", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  평균  : {avg:.2f}", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  최저  : {lo:.2f}", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  최고  : {hi:.2f}", WIDTH - 2) + "│")
            print("└" + border + "┘")

    def main():
        while True:
            show_menu()
            choice = input('선택: ').strip()
            if choice == '0':
                print('프로그램을 종료합니다.')
                break
            calculate(choice)
            input('\n계속하려면 Enter를 눌러주세요...')

    main()