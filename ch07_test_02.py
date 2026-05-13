#=======================================================================
# 파일명 : ch07_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-05-06
#=======================================================================

#항상 넣는 코드들 (화면 초기화, 시각적 너비 계산, 시각적 정렬)
import os
import subprocess

#os.system은 deprecated 됨, subprocess.run으로 변경
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

#clear_screen() #실행 결과 캡처를 위해서 주석처리

# 프로그램 선택 메뉴
border = "─" * (WIDTH - 2)

print("┌" + border + "┐")
print("│" + vis_center("프로그램 목록", WIDTH - 2) + "│")
print("├" + border + "┤")
print("│" + vis_ljust("  1. ch07_01_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  2. ch07_01_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  3. ch07_01_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  4. ch07_01_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  5. tuple_practice.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  6. ch07_02_1~3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  7. ch07_02_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  8. dict_practice.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  9. ch07_03_1~2.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 10. ch07_03_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 11. ch07_03_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 12. set_practice.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 13. ch07_04_1.py", WIDTH - 2) + "│")
print("└" + border + "┘")

selected_program = int(input("프로그램 번호를 입력하세요: "))

#ch07_01_1.py
if selected_program == 1:
    # 리스트: 대괄호
    fruits_list = ["사과", "바나나", "포도"]
    # 튜플: 소괄호
    fruits_tuple = ("사과", "바나나", "포도")
    print(type(fruits_list))   # <class 'list'>
    print(type(fruits_tuple))  # <class 'tuple'>

#ch07_01_2.py
if selected_program == 2:
    # 요소 1개 튜플 선언 방법
    a = (5)      # 정수 5 (튜플 아님!)
    b = (5,)     # 진짜 튜플 — 뒤에 콤마 필수
    c = 5,       # 소괄호 없이 콤마만으로도 OK
    print(type(a))   # <class 'int'>
    print(type(b))   # <class 'tuple'>
    print(type(c))   # <class 'tuple'>

#ch07_01_3.py
if selected_program == 3:
    # 튜플은 요소의 변경, 추가, 삭제가 불가능한 자료형
    fruits = ("사과", "바나나", "포도")
    print(fruits[0])         # 사과 — 읽기OK
    print(fruits[1:3])       # ('바나나', '포도') — 슬라이싱OK
    #fruits[0] = "키위"        # TypeError! — 수정불가
    #fruits.append("딸기")      # AttributeError! — 추가불가

#ch07_01_4.py
if selected_program == 4:
    # 튜플 언패킹 예제
    person = ("홍길동", 20, "서울")
    name, age, city = person   # 언패킹
    print(f"이름: {name}")      # 이름: 홍길동
    print(f"나이: {age}")       # 나이: 20
    # 변수 교환을 한줄로
    a, b = 10, 20
    a, b = b, a                # 튜플 언패킹 원리
    print(f"a={a}, b={b}")     # a=20, b=10

#tuple_practice.py
if selected_program == 5:
    from datetime import datetime, timezone, timedelta

    # 1. 요일 튜플과 인덱싱
    weekdays = ("월","화","수","목","금","토","일")
    kst = datetime.now(timezone.utc) + timedelta(hours=9) #한국 시간 KST 기준(UTC+9)
    today_weekday = kst.weekday()  # 월요일=0, 일요일=6
    print(f"오늘은 {weekdays[today_weekday]}요일!")
    # 2. 언패킹으로 학생 정보 출력
    student = ("유진혁", 23, "컴퓨터시스템공학")
    name, age, major = student
    print(f"{name} ({age}세) -{major}과")
    # 3. 변수 교환
    x, y = 100, 200
    x, y = y, x
    print(f"교환 후: x={x}, y={y}")

# ch07_02_1~3.py
if selected_program == 6:
    # 전화번호부 딕셔너리
    phone_book = {
    "김철수": "010-1234-5678",
    "이영희": "010-2345-6789",
    "박민수": "010-3456-7890",
    }
    print(type(phone_book))   # <class 'dict'>
    print(phone_book["김철수"])    # 010-1234-5678
    # 없는키 → KeyError 발생!
    # print(phone_book["최유리"])   # KeyError!
    # 안전하게 조회: get(키, 기본값)
    result = phone_book.get("최유리", "번호없음")
    print(result)
    modified_result = input("수정된 결과도 확인하시겠습니까? (y/n): ").strip().lower()
    if modified_result == 'y':
        phone = {"김철수": "010-1111-1111"}
        # 추가(새키)
        phone["이영희"] = "010-2222-2222"
        # 수정(기존키)
        phone["김철수"] = "010-9999-9999"
        # 삭제: del
        del phone["이영희"]
        # 삭제 후 값반환: pop()
        removed = phone.pop("김철수")
        print(f"삭제된 번호: {removed}")
    if modified_result == 'n':
        print("수정된 결과는 확인하지 않겠습니다.")

# ch07_02_4.py
if selected_program == 7:
    prices = {"사과": 1500, "바나나": 800, "포도": 3000}
    # keys() / values() / items()
    print(list(prices.keys()))    # ['사과', '바나나', '포도']
    print(list(prices.values()))  # [1500, 800, 3000]
    # items() + 언패킹 — 가장 편리함
    for fruit, price in prices.items():
        print(f"{fruit}: {price}원")

# dict_practice.py — 과일 가격표 관리
if selected_program == 8:
    shop = {}
    shop["사과"] = 1500
    shop["바나나"] = 800
    shop["포도"] = 3000
    shop["딸기"] = 2500

    title = "과일 가격표"
    border = "─" * (WIDTH - 2)

    print("┌" + border + "┐")
    print("│" + vis_center(title, WIDTH - 2) + "│")
    print("├" + border + "┤")
    #과일 목록
    for name, price in shop.items():
        #과일명은 왼쪽 정렬, 가격은 오른쪽 정렬
        name_width = 10
        price_str = f"{price:,}원"
        line = vis_ljust(name, name_width) + vis_rjust(price_str, WIDTH - 2 - name_width)
        print("│" + line + "│")
    # 하단 테두리
    print("└" + border + "┘")

    # 가격조회(get 활용)
    print(f"\n포도 가격: {shop.get('포도', '미등록')}원")

# ch07_03_1~2.py
if selected_program == 9:
    # 집합 만들기 — { } 사용
    fruits = {"사과", "바나나", "포도"}
    print(type(fruits))   # <class 'set'>
    # 중복 자동 제거!
    numbers = {1, 3, 5, 3, 7, 1, 9, 5}
    print(numbers)        # {1, 3, 5, 7, 9}
    a = {}        # 빈 딕셔너리(dict)
    b = set()     # 빈 집합(set)
    print(type(a))   # <class 'dict'>
    print(type(b))   # <class 'set'>

# ch07_03_3.py
if selected_program == 10:
    #중복 제거 예제
    scores = [85, 92, 78, 85, 95, 78, 92, 88]
    unique = list(set(scores))   # 중복 제거!
    print(unique)                # [78, 85, 88, 92, 95] (순서 다를 수 있음)

# ch07_03_4.py
if selected_program == 11:
    # 집합 연산 예제
    a = {"사과", "바나나", "포도", "딸기"}
    b = {"포도", "딸기", "망고", "키위"}
    print(f"합집합: {a | b}")        # 모두 포함
    print(f"교집합: {a & b}")        # 공통만
    print(f"차집합(a-b): {a - b}")   # a에만 있는것
    print(f"대칭 차집합: {a ^ b}")    # 한쪽에만

# set_practice.py — 출석부 관리
if selected_program == 12:
    monday = {"김철수", "이영희", "박민수", "최유리"}
    tuesday = {"김철수", "박민수", "한지우", "오준서"}

    border = "─" * (WIDTH - 2)

    print("┌" + border + "┐")
    print("│" + vis_center("출석부 관리", WIDTH - 2) + "│")
    print("├" + border + "┤")

    print("│" + vis_ljust("월요일 출석", 10) + ": " + vis_ljust(", ".join(sorted(monday)), WIDTH - 2 - 10 - 3) + "│")
    print("│" + vis_ljust("화요일 출석", 10) + ": " + vis_ljust(", ".join(sorted(tuesday)), WIDTH - 2 - 10 - 3) + "│")

    print("├" + border + "┤")

    print("│" + vis_ljust("양일 모두", 13) + ": " + vis_ljust(", ".join(sorted(monday & tuesday)), WIDTH - 2 - 13 - 2) + "│")
    print("│" + vis_ljust("월요일만", 13) + ": " + vis_ljust(", ".join(sorted(monday - tuesday)), WIDTH - 2 - 13 - 2) + "│")
    print("│" + vis_ljust("전체 학생수", 13) + ": " + vis_ljust(str(len(monday | tuesday)) + "명", WIDTH - 2 - 13 - 2) + "│")
    print("└" + border + "┘")

# ch07_04_1.py
if selected_program == 13:
    my_list = [1, 2, 3, 4, 5]
    my_tuple = tuple(my_list)   # 리스트 → 튜플
    my_set   = set(my_list)     # 리스트 → 집합(중복제거)
    print(my_list) ; print(my_tuple) ; print(my_set)
    # 리스트 중복 제거 실전 패턴
    nums = [1, 3, 5, 3, 7, 1]
    unique = list(set(nums))
    print(unique)               # [1, 3, 5, 7]
    # 딕셔너리의 키/값을리스트로
    prices = {"사과": 1500, "바나나": 800}
    keys = list(prices.keys())   # ['사과', '바나나']
    vals = list(prices.values()) # [1500, 800]
    print(prices) ; print(keys) ; print(vals)