#=======================================================================
# 파일명 : ch06_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-04-29
#=======================================================================

#항상 넣는 코드들 (화면 초기화, 시각적 너비 계산, 시각적 정렬)
import os

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')

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

#초기 화면
clear_screen()
print("┌" + "─" * (WIDTH - 2) + "┐")
print("│" + vis_center("ch06_test_01.py", WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")
print("│" + vis_ljust("프로그램을 선택해주세요.", WIDTH - 2) + "│")
print("└" + "─" * (WIDTH - 2) + "┘")

# 프로그램 목록 UI
programs = [
    "1. ch06_01_1.py - 변수 여러개 vs 리스트",
    "2. ch06_02_1.py - 리스트 생성",
    "3. ch06_02_2.py - 리스트 인덱싱",
    "4. ch06_02_3.py - len() 함수",
    "5. ch06_03_1.py - 슬라이싱",
    "6. ch06_04_1.py - 요소 변경",
    "7. ch06_04_2.py - append, insert",
    "8. ch06_04_3.py - append vs extend",
    "9. ch06_04_4.py - extend vs +",
    "10. ch06_04_5.py - 삭제 (del, remove, pop)",
    "11. ch06_05_1.py - sort",
    "12. ch06_05_2.py - index, count, in",
    "13. ch06_05_3.py - copy",
    "14. ch06_05_4.py - clear",
    "15. ch06_06_1.py - for 루프",
    "16. ch06_06_2.py - 합계 평균, 조건 모으기",
    "17. ch06_06_3.py - 패턴 예시",
    "18. ch06_06_4.py - enumerate",
    "19. ch06_06_5.py - 학생수 입력받아 리스트 만들기",
    "20. ch06_06_6.py - quit까지 입력",
    "21. ch06_07_1.py - len, sum, max, min",
    "22. ch06_07_2.py - sorted",
    "23. ch06_08_1.py - 2차원 리스트",
    "24. ch06_08_2.py - 2차원 루프",
    "25. ch06_08_3.py - 리스트 컴프리헨션",
    "26. ???"
]

print("┌" + "─" * (WIDTH - 2) + "┐")
print("│" + vis_center("프로그램 목록", WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")
for prog in programs:
    print("│" + vis_ljust(f"  {prog}", WIDTH - 2) + "│")
print("└" + "─" * (WIDTH - 2) + "┘")

selected_program = int(input("프로그램 번호 입력: "))

#ch06_01_1.py
if selected_program == 1:
    # 방법1: 변수여러개(비효율적)
    score1 = 85 ; score2 = 92 ; score3 = 78
    total = score1 + score2 + score3 #학생 많을때 계산하기 어려움
    print(f'평균: {total / 3}')
    # 방법2: 리스트(효율적!)
    scores = [85, 92, 78, 88, 95, 71]
    total = sum(scores) # 학생이 몇명이든 동일!
    print(f'합계: {total}, 평균: {total / len(scores):.1f}')

#ch06_02_1.py
if selected_program == 2:
    fruits = ['사과', '바나나', '포도', '딸기']  # 문자열리스트
    numbers = [10, 20, 30, 40, 50]            # 숫자리스트
    mixed = [1, 3.14, '파이썬', True]          # 혼합리스트
    empty = []                                # 빈리스트
    print(fruits) ;print(numbers);print(mixed);print(empty)
    # 리스트 안에 리스트도 가능! (2차원리스트—6.8에서자세히)
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrix)

#ch06_02_2.py
if selected_program == 3:
    fruits = ['사과', '바나나', '포도', '딸기']
    print(fruits[0])    # → 사과(첫번째)
    print(fruits[2])    # → 포도(세번째)
    print(fruits[-1])   # → 딸기(마지막)
    print(len(fruits))  # → 4 (길이)

#ch06_02_3.py
if selected_program == 4:
    fruits = ['사과', '바나나', '포도', '딸기']
    print(len(fruits))  # → 4
    empty = []
    print(len(empty))   # → 0

#ch06_03_1.py
if selected_program == 5:
    numbers = [10, 20, 30, 40, 50, 60, 70]
    print(numbers[1:4])   # → [20, 30, 40]
    print(numbers[:3])    # → [10, 20, 30]  (처음부터)
    print(numbers[4:])    # → [50, 60, 70]  (끝까지)
    print(numbers[:])     # → [10,20,30,40,50,60,70]  (전체복사)
    print(numbers[::2])   # → [10, 30, 50, 70]  (2칸씩)
    print(numbers[::-1])  # → [70,60,50,40,30,20,10]  (뒤집기!)

#ch06_04_1.py
if selected_program == 6:
    scores = [85, 92, 78, 88, 95]
    scores[2] = 90   # 78 → 90으로변경
    scores[-1] = 100 # 마지막값변경
    print(scores)    # → [85, 92, 90, 88, 100]

#ch06_04_2.py
if selected_program == 7:
    fruits = ['사과', '바나나']
    fruits.append('포도')      # 맨뒤에추가
    fruits.insert(1, '망고')   # 인덱스1에끼워넣기
    print(fruits)  # → ['사과', '망고', '바나나', '포도']

#ch06_04_3.py
if selected_program == 8:
    a = [1, 2, 3]
    a.append([4, 5])  # → [1, 2, 3, [4, 5]] 리스트가통째로!
    print(f"append= {a}")
    a = [1, 2, 3]
    a.extend([4, 5])  # → [1, 2, 3, 4, 5]  값이하나씩!
    print(f"extend= {a}")

#ch06_04_4.py
if selected_program == 9:
    a = [1, 2, 3]
    b = [4, 5, 6]
    # extend(): 원본에다른리스트값을하나씩추가
    a.extend(b)
    print(a)  # → [1, 2, 3, 4, 5, 6]
    # + 연산자: 두리스트를합쳐새리스트생성
    c = [1, 2, 3] + [4, 5, 6]
    print(c)  # → [1, 2, 3, 4, 5, 6]

#ch06_04_5.py
if selected_program == 10:
    fruits = ['사과', '바나나', '포도', '딸기']
    del fruits[1]        # 인덱스로 삭제(바나나삭제)
    fruits.remove('포도') # 값으로 삭제
    last = fruits.pop()  # 마지막값 꺼내면서 삭제
    print(last)          # → 딸기
    print(fruits)        # → ['사과']
    better_program = input("더 나은 예시 프로그램도 출력하시겠습니까? (y/n): ").strip().lower()
    #ch06_04_5_1.py
    if better_program == 'y':
        fruits = ['사과', '바나나', '포도', '딸기']
        del fruits[1]        # 인덱스로 삭제(바나나삭제)
        fruits.remove('포도') # 값으로 삭제
        print(fruits.pop())# 마지막 값 꺼내면서 삭제
        #fruits.pop()에서→ 딸기 삭제
        print(fruits)        # → ['사과']
    else:
        print("더 나은 예시 프로그램을 출력하지 않습니다.")

#ch06_05_1.py
if selected_program == 11:
    numbers = [64, 25, 12, 22, 11]
    numbers.sort()              # 오름차순정렬(원본변경!)
    print(numbers)              # → [11, 12, 22, 25, 64]
    numbers.sort(reverse=True)  # 내림차순
    print(numbers)              # → [64, 25, 22, 12, 11]
    fruits = ['다영', '수진', '가연', '나리']
    fruits.sort()               # 가나다순정렬
    print(fruits)           # ['가연', '나리', '다영', '수진’]

#ch06_05_2.py
if selected_program == 12:
    fruits = ['사과', '바나나', '포도', '바나나']
    print(fruits.index('포도'))    # → 2 (위치찾기)
    print(fruits.count('바나나'))  # → 2 (개수세기)
    print('망고' in fruits)        # → False (있는지확인)
    print('사과' not in fruits)    # → False

#ch06_05_3.py
if selected_program == 13:
    a = [1, 2, 3]
    b = a          # 같은리스트를가리킴!
    b[0] = 999
    print(a)       # → [999, 2, 3]  a도바뀜!
    a = [1, 2, 3]
    b = a.copy()   # 독립된복사본
    b[0] = 999
    print(a)       # → [1, 2, 3]  a는그대로!

#ch06_05_4.py
if selected_program == 14:
    a = [1, 2, 3]
    a.clear()             # 리스트의모든요소삭제
    print(a)              # → []  a는빈리스트가됨

#ch06_06_1.py
if selected_program == 15:
    fruits = ['사과', '바나나', '포도', '딸기']
    for fruit in fruits:   # 값을하나씩꺼냄
        print(f"나는{fruit}을좋아해요!")

#ch06_06_2.py
if selected_program == 16:
    scores = [85, 92, 78, 88, 95, 70, 91, 62]
    # 합계와평균
    total = 0
    for score in scores:
        total += score
    print(f'평균: {total/len(scores):.1f}')
    # 조건에맞는값모으기(핵심패턴!)
    high = []                    # 빈리스트준비
    for score in scores:
        if score >= 90:
            high.append(score)
    print(f'90점이상: {high}')  # → [92, 95, 91]

#ch06_06_3.py
if selected_program == 17:
    scores = [85, 92, 78, 88, 95, 70, 91, 62]
    # 패턴예시1: 90점이상만모으기
    high = []
    for score in scores:
        if score >= 90:
            high.append(score)
    print(f'90점이상: {high}')
    # 패턴예시2: 짝수만모으기
    evens = []
    for x in scores:
        if x % 2 == 0:
            evens.append(x)
    print(f'짝수점수: {evens}')

#ch06_06_4.py
if selected_program == 18:
    students = ['김철수', '이영희', '박민수']
    # enumerate 없이(번거로움)
    i = 0
    for name in students:
        print(f'{i+1}번: {name}')
        i += 1
    # enumerate 사용(깔끔!)
    for num, name in enumerate(students, start=1): 
            print(f'{num}번: {name}')
    for num, name in enumerate(students, start=2): #번호를 수정하더라도 읽는 순서는 변하지 않음
            print(f"{num}번: {name}")

#ch06_06_5.py
if selected_program == 19:
    # 학생수를먼저입력받아리스트만들기
    scores = []
    count = int(input('학생수를 입력하세요: '))
    for i in range(count):
        score = int(input(f'{i+1}번 학생 점수: '))
        scores.append(score)
    print(f'입력한 점수: {scores}')
    print(f'평균: {sum(scores)/len(scores):.1f}')

#ch06_06_6.py
if selected_program == 20:
    # 'quit' 입력까지계속받기
    names = []
    while True:
        name = input('이름(그만하려면quit): ')
        if name == 'quit':
            break
        names.append(name)
        print(f'입력한이름: {names}, 총{len(names)}명')

#ch06_07_1.py
if selected_program == 21:
    scores = [85, 92, 78, 88, 95, 70, 91, 62]
    print(f'학생수: {len(scores)}명')           # → 8명
    print(f'합계: {sum(scores)}점')            # → 661점
    print(f'평균: {sum(scores)/len(scores):.1f}점') # → 82.6점
    print(f'최고점: {max(scores)}점')           # → 95점
    print(f'최저점: {min(scores)}점')           # → 62점
    print(f'점수범위: {max(scores)-min(scores)}점')  # → 33점

#ch06_07_2.py
if selected_program == 22:
    original = [64, 25, 12, 22, 11]
    # sorted(): 원본유지, 새리스트반환
    asc  = sorted(original)              # 오름차순새리스트
    desc = sorted(original, reverse=True) # 내림차순새리스트
    print(f'원본: {original}')            # 원본그대로!
    print(f'오름차순: {asc}')
    print(f'내림차순: {desc}')

#ch06_08_1.py
if selected_program == 23:
    # 3명의학생, 3과목점수표
    grades = [
    [85, 90, 78],  # 김철수: [국어, 영어, 수학]
    [92, 88, 95],  # 이영희
    [76, 82, 89],  # 박민수
    ]
    print(grades[0])     # → [85, 90, 78] (김철수전체)
    print(grades[0][1])  # → 90 (김철수 영어)
    print(grades[2][2])  # → 89 (박민수 수학)

#ch06_08_2.py\
if selected_program == 24:
    names    = ['김철수', '이영희', '박민수']
    subjects = ['국어', '영어', '수학']
    grades   = [[85,90,78],[92,88,95],[76,82,89]]
    # 학생별평균(바깥for문만)
    for i, row in enumerate(grades):
        avg = sum(row) / len(row)
        print(f'{names[i]}: 평균{avg:.1f}')
    # 개별점수(이중for문)
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            print(f'{names[i]} {subjects[j]}: {grades[i][j]}점')

#ch06_08_3.py
if selected_program == 25:
    # 잘못된방법(참조복사!)
    matrix = [[0] * 3] * 3
    matrix[0][0] = 99
    print(matrix)   # [[99,0,0],[99,0,0],[99,0,0]] 모두바뀜!
    # 올바른방법(리스트컴프리헨션)
    matrix = [[0] * 3 for _ in range(3)]
    matrix[0][0] = 99
    print(matrix)   # [[99,0,0],[0,0,0],[0,0,0]] 하나만!

if selected_program == 26:
    clear_screen()
    print("숨겨진 항목에 오신 것을 환영합니다.")
    secret_program = input("비밀 프로그램 코드를 입력해주세요.:  ")
    #list_index.py
    if secret_program == "list_index":
        foods = ['피자', '치킨', '햄버거', '라면', '부대찌개']
        print(f'첫번째: {foods[0]}')
        print(f'마지막: {foods[-1]}')
        print(f'총{len(foods)}개의음식')
    
    #list_slice.py
    if secret_program == "list_slice":
        colors = ['빨강','주황','노랑','초록','파랑','남색','보라']
        warm = colors[:3]       # 따뜻한색
        cool = colors[3:]       # 차가운색
        every_other = colors[::2]  # 하나건너
        rev = colors[::-1]      # 뒤집기
        print(warm, cool, every_other, rev)
        #노랑, 초록, 파랑
        print(colors[2:5])

    #list_modify.py
    if secret_program == "list_modify":
        shopping = ['우유', '빵', '계란']
        shopping.append('치즈')    # 맨뒤추가
        shopping.insert(0, '사과') # 맨앞삽입
        shopping.remove('빵')      # 빵삭제
        last = shopping.pop()      # 마지막꺼내기
        print(f'꺼낸것: {last}, 남은것: {shopping}')
    
    #list_methods.py
    if secret_program == "list_methods":
        scores = [78, 95, 62, 88, 73, 95, 81]
        scores.sort()                    # 오름차순정렬
        print(f'정렬: {scores}')
        print(f'95점개수: {scores.count(95)}개')
        print(f'62점위치: 인덱스{scores.index(62)}')
        if 62 in scores:
            scores.remove(62)            # 안전하게삭제
        print(f'62 삭제후: {scores}')

    #list_loop.py
    if secret_program == "list_loop":
        scores = [85, 92, 78, 65, 95, 88, 72, 91, 60, 83]
        grade_a, grade_f = [], []
        for score in scores:
            if score >= 90: grade_a.append(score)
            elif score < 70: grade_f.append(score)
        print(f'A등급({len(grade_a)}명): {grade_a}')
        print(f'F등급({len(grade_f)}명): {grade_f}')
        for i, score in enumerate(scores, start=1):
            print(f'{i}번 학생 점수: {score}, 등급: {"A" if score >= 90 else "B" if score >= 70 else "C" if score >= 60 else "F"}')
        
    #list_builtin.py
    if secret_program == "list_builtin":
        sales = [1200,1500,980,1800,2100,1650,1400,1900,2300,1750,2000,2500]
        months = ['1월','2월','3월','4월','5월','6월',
        '7월','8월','9월','10월','11월','12월']
        print(f'총 매출: {sum(sales):,}만원')
        print(f'월 평균: {sum(sales)/len(sales):,.1f}만원')
        best_idx = sales.index(max(sales))
        print(f'최고 매출월: {months[best_idx]}')
    
    #list_2d.py
    if secret_program == "list_2d":
        grades = [[85,90,78],[92,88,95],[76,82,89]]
        names  = ['김철수','이영희','박민수']
        # 학생 별 평균 출력
        for i in range(len(names)):
            avg = sum(grades[i]) / len(grades[i])
            print(f'{names[i]}: {grades[i]} → 평균{avg:.1f}')
        # 전체 최고점을 받은 학생과 점수를 찾아 출력하기
        best_score = 0
        best_student = ""
        for i in range(len(grades)):
            for j in range(len(grades[i])):
                if grades[i][j] > best_score:
                    best_score = grades[i][j]
                    best_student = names[i]
        print(f'전체 최고점 학생: {best_student}, 점수: {best_score}')
    
    #grade_manager.py
    if secret_program == "grade_manager":
        names = []
        scores = []

        def print_menu():
            clear_screen()
            print("┌" + "─" * (WIDTH - 2) + "┐")
            print("│" + vis_center("성적 관리 프로그램", WIDTH - 2) + "│")
            print("├" + "─" * (WIDTH - 2) + "┤")
            print("│" + vis_ljust("  1. 입력", WIDTH - 2) + "│")
            print("│" + vis_ljust("  2. 전체보기", WIDTH - 2) + "│")
            print("│" + vis_ljust("  3. 통계", WIDTH - 2) + "│")
            print("│" + vis_ljust("  4. 수정", WIDTH - 2) + "│")
            print("│" + vis_ljust("  5. 삭제", WIDTH - 2) + "│")
            print("│" + vis_ljust("  6. 종료", WIDTH - 2) + "│")
            print("└" + "─" * (WIDTH - 2) + "┘")

        while True:
            print_menu()
            choice = input("메뉴 선택: ")

            if choice == '1':   # 입력
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("학생 입력", WIDTH - 2) + "│")
                print("├" + "─" * (WIDTH - 2) + "┤")
                name  = input("│  학생 이름: ")
                score = int(input("│  점수(0-100): "))
                if 0 <= score <= 100:
                    names.append(name)
                    scores.append(score)
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust(f"   {name}({score}점) 등록 완료!", WIDTH - 2) + "│")
                else:
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust("   점수는 0~100 사이여야 합니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                input("  엔터를 누르면 메뉴로 돌아갑니다.")

            elif choice == '2': # 전체보기
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("전체 학생 목록", WIDTH - 2) + "│")
                print("├" + "─" * (WIDTH - 2) + "┤")
                if names:
                    for i, (name, score) in enumerate(zip(names, scores), 1):
                        grade = 'A' if score>=90 else 'B' if score>=80 else 'C' if score>=70 else 'F'
                        print("│" + vis_ljust(f"  {i}. {name}: {score}점 ({grade})", WIDTH - 2) + "│")
                else:
                    print("│" + vis_ljust("  등록된 학생이 없습니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                input("  엔터를 누르면 메뉴로 돌아갑니다.")

            elif choice == '3': # 통계
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("성적 통계", WIDTH - 2) + "│")
                print("├" + "─" * (WIDTH - 2) + "┤")
                if scores:
                    print("│" + vis_ljust(f"  평균: {sum(scores)/len(scores):.1f}점", WIDTH - 2) + "│")
                    print("│" + vis_ljust(f"  최고: {max(scores)}점", WIDTH - 2) + "│")
                    print("│" + vis_ljust(f"  최저: {min(scores)}점", WIDTH - 2) + "│")
                else:
                    print("│" + vis_ljust("  등록된 학생이 없습니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                input("  엔터를 누르면 메뉴로 돌아갑니다.")

            elif choice == '4': # 수정
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("학생 점수 수정", WIDTH - 2) + "│")
                print("├" + "─" * (WIDTH - 2) + "┤")
                target = input("│  수정할 학생 이름: ")
                if target in names:
                    idx = names.index(target)
                    scores[idx] = int(input("│  새 점수: "))
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust(f"   {target} 점수 수정 완료!", WIDTH - 2) + "│")
                else:
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust("   해당 학생을 찾을 수 없습니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                input("  엔터를 누르면 메뉴로 돌아갑니다...")

            elif choice == '5': # 삭제
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("학생 삭제", WIDTH - 2) + "│")
                print("├" + "─" * (WIDTH - 2) + "┤")
                target = input("│  삭제할 학생 이름: ")
                if target in names:
                    idx = names.index(target)
                    names.pop(idx)
                    scores.pop(idx)
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust(f"   {target} 삭제 완료!", WIDTH - 2) + "│")
                else:
                    print("├" + "─" * (WIDTH - 2) + "┤")
                    print("│" + vis_ljust("   해당 학생을 찾을 수 없습니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                input("  엔터를 누르면 메뉴로 돌아갑니다.")

            elif choice == '6': # 종료
                clear_screen()
                print("┌" + "─" * (WIDTH - 2) + "┐")
                print("│" + vis_center("프로그램을 종료합니다.", WIDTH - 2) + "│")
                print("└" + "─" * (WIDTH - 2) + "┘")
                break
