#=======================================================================
# 파일명 : ch09_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-05-20
#=======================================================================

#항상 넣는 코드들 (화면 초기화, 시각적 너비 계산, 시각적 정렬)
from fileinput import filename  
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
WIDTH = 60

clear_screen()

border = "─" * (WIDTH - 2)

print("┌" + border + "┐")
print("│" + vis_center("프로그램 목록", WIDTH - 2) + "│")
print("├" + border + "┤")
print("│" + vis_ljust("  1. ch09_01_1.py   11. ch09_04_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  2. ch09_02_1.py   12. ch09_04_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  3. ch09_02_2.py   13. ch09_05_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  4. ch09_02_3.py   14. ch09_05_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  5. ch09_03_1.py   15. ch09_06_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  6. ch09_03_2.py   16. ch09_06_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  7. ch09_03_3.py   17. ch09_07_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  8. ch09_03_4.py   18. ch09_07_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  9. ch09_04_1.py   19. ch09_07_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 10. ch09_04_2.py   20. my_memo.py", WIDTH - 2) + "│")
print("└" + border + "┘")
print()

selected_program = int(input("실행할 프로그램 입력 : "))

# ch09_01_1.py
if selected_program == 1 :
    #파일 입출력 기본 3단계
    f = open("D:/Python/Data/hello.txt", "w", encoding="utf-8")  # 1단계: 열기
    f.write("안녕하세요!")        # 2단계: 쓰기
    f.close()                   # 3단계: 닫기

# ch09_02_1.py
if selected_program == 2 :
    #write()로 파일 만들기
    f = open("D:/Python/Data/diary.txt", "w", encoding="utf-8")
    f.write("첫번째 줄\n")
    f.write("두번째 줄\n")
    f.write("세번째 줄\n")
    f.close()

# ch09_02_2.py
if selected_program == 3 :
    # print()로 파일 쓰기 — 자동 줄바꿈!
    f = open("D:/Python/Data/score_report.txt", "w", encoding="utf-8") #인코딩 설정
    students = [("김철수", 85), ("이영희", 92), ("박민수", 78)]
    print("=== 학생 성적표 ===", file=f)
    for name, score in students:
        print(f"{name}: {score}점", file=f)
    f.close()
    print("저장 완료!")

# ch09_02_3.py
# 자기소개 파일 만들기
if selected_program == 4 :
    f = open("D:/Python/Data/intro.txt", "w", encoding="utf-8") #인코딩 설정 안하면 한글 깨짐
    name = input("이름: ")
    age = int(input("나이: "))
    print("=== 자기소개===", file=f)
    print(f"이름: {name}", file=f)
    print(f"나이: {age}살", file=f)
    print(f"태어난 해: {2026 -age}년", file=f)
    f.close()
    print("intro.txt 생성 완료!")

# ch09_03_1.py
if selected_program == 5 :
    # 테스트 파일 미리 만들기
    with open("D:/Python/Data/fruits.txt", "w", encoding="utf-8") as f:
        f.write("사과\n바나나\n딸기\n포도\n수박\n")
    # ① read() — 전체를 하나의 문자열로
    f = open("D:/Python/Data/fruits.txt", "r", encoding="utf-8")
    content = f.read()  # 전체 내용을 한번에
    f.close()
    print(content)

# ch09_03_2.py
if selected_program == 6 :
    # ② readlines() — 모든 줄을 리스트로
    f = open("D:/Python/Data/fruits.txt", "r", encoding="utf-8")
    lines = f.readlines()  # ["사과\n", "바나나\n", ...]
    f.close()
    fruits = [line.strip() for line in lines]
    print(fruits)  # ['사과', '바나나', '딸기', ...]

    # ③ for문으로 직접 읽기 — 가장 파이썬다운 방법!
    f = open("D:/Python/Data/fruits.txt", "r", encoding="utf-8")
    for line in f:
        print(line.strip())
    f.close()

# ch09_03_3.py
if selected_program == 7 : 
    # 쓰기 : 쉼표로 구분
    with open("D:/Python/Data/menu.txt", "w", encoding="utf-8") as f:
        f.write("아메리카노,4500\n카페라떼,5000\n카푸치노,5500\n")
    # 읽기 : split(",")으로 분리
    with open("D:/Python/Data/menu.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, price = line.strip().split(",")
            print(f"{name}: {int(price):,}원")

# ch09_03_4.py
if selected_program == 8 :
    # 카페 메뉴판 만들기
    with open("D:/Python/Data/menu.txt", "r", encoding="utf-8") as f:
        print("카페 메뉴판")
        print("-" * 25)
        for i, line in enumerate(f, 1):
            name, price = line.strip().split(",")
            print(f" {i}. {name:8s} {int(price):,}원")
    print("-" * 25)

# ch09_04_1.py
if selected_program == 9 : 
    # [Before] 기존방식 — close() 직접 호출
    f = open("D:/Python/Data/diary.txt", "w", encoding="utf-8")
    f.write("오늘의 일기\n")
    f.close()  # 깜빡하면 문제 발생

# ch09_04_2.py
if selected_program == 10 : 
    # [After] with문 — 자동으로 닫아줌
    with open("D:/Python/Data/diary.txt", "w", encoding="utf-8") as f:
        f.write("오늘의 일기\n")
        f.write("파이썬 공부를 했다.\n")
    # with 블록을 벗어나면 자동으로 f.close() 실행!

# ch09_04_3.py
if selected_program == 11 :
    # with문으로 쓰기와 읽기 연결하기
    with open("D:/Python/Data/scores.txt", "w", encoding="utf-8") as f:
        print("김철수, 85", file=f)
        print("이영희, 92", file=f)
        print("박민수, 78", file=f)

    students = []
    with open("D:/Python/Data/scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, score = line.strip().split(",")
            students.append((name, int(score)))
    # with 블록 밖에서 데이터 활용 (파일은 이미 닫힘 )
    for name, score in students:
        print(f"{name}: {score}점")
    print(f"평균: {sum(s for _,s in students)/len(students):.1f}점")

# ch09_04_4.py
if selected_program == 12 :
    # with문으로 자기소개 파일 만들기
    name = input("이름: ")
    age = int(input("나이: "))
    with open("D:/Python/Data/about_me.txt", "w", encoding="utf-8") as f:
        print("=== 자기소개 ===", file=f)
        print(f"이름: {name}", file=f)
        print(f"나이: {age}살", file=f)
    with open("D:/Python/Data/about_me.txt", "r", encoding="utf-8") as f:
        print(f.read())

# ch09_05_1.py
if selected_program == 13 :
    # 'w' 모드: 기존내용이삭제되는것을확인
    with open("D:/Python/Data/test.txt", "w", encoding="utf-8") as f:
        f.write("원래 내용\n중요한 데이터\n")
    with open("D:/Python/Data/test.txt", "w", encoding="utf-8") as f:  # 다시 열면?
        f.write("새로운 내용\n")  # 원래내용이 모두 사라짐!
    # 'a' 모드: 기존 내용 유지하며 추가
    with open("D:/Python/Data/log.txt", "w", encoding="utf-8") as f:
        f.write("[1일차] 파이썬 공부 시작\n")
    with open("D:/Python/Data/log.txt", "a", encoding="utf-8") as f:
        f.write("[2일차] 변수와 자료형 학습\n")
    with open("D:/Python/Data/log.txt", "a", encoding="utf-8") as f:
        f.write("[3일차] 조건문, 반복문 학습\n")
    with open("D:/Python/Data/log.txt", "r", encoding="utf-8") as f:
        print(f.read())

# ch09_05_2.py
if selected_program == 14 :
    # 파일모드실험
    with open('D:/Python/Data/mode_test.txt', 'w', encoding='utf-8') as f:
        f.write('1번째: w 모드로 생성\n 2번째: 처음 내용\n')
    with open('D:/Python/Data/mode_test.txt', 'a', encoding='utf-8') as f:
        f.write('3번째: a 모드로 추가\n')
    with open('D:/Python/Data/mode_test.txt', 'r', encoding='utf-8') as f:
        print(f.read())  # 3줄모두출력
    with open('D:/Python/Data/mode_test.txt', 'w', encoding='utf-8') as f:
        f.write('w 모드는 초기화!\n')
    with open('D:/Python/Data/mode_test.txt', 'r', encoding='utf-8') as f:
        print(f.read())  # 마지막줄만 출력!

# ch09_06_1.py
if selected_program == 15 :
    # 테스트 데이터 파일 생성
    with open("D:/Python/Data/all_scores.txt", "w", encoding="utf-8") as f:
        f.write("김철수,85\n이영희,92\n박민수,45\n정다은,96\n최준호,58\n")
    # 패턴1: 읽기 + 변환 + 계산
    total = 0
    count = 0
    with open("D:/Python/Data/all_scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, score = line.strip().split(",")
    total += int(score)
    count += 1
    print(f"평균: {total/count:.1f}점")
    # 패턴2: 조건 필터링 (60점 미만 찾기)
    with open("D:/Python/Data/all_scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, score = line.strip().split(",")
            if int(score) < 60:
                print(f"재시험 대상: {name} ({score}점)")
    # 패턴3: 파일 → 리스트 → 다양한 처리
    students = []
    with open("D:/Python/Data/all_scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, score = line.strip().split(",")
    students.append((name, int(score)))
    # 정렬 등 다양한 가공 가능
    students.sort(key=lambda x: x[1], reverse=True)
    for rank, (name, score) in enumerate(students, 1):
        print(f"{rank}등: {name} ({score}점)")
    # 패턴4: 파일 → 가공 → 새파일
    with open("D:/Python/Data/all_scores.txt", "r", encoding="utf-8") as fin:
        with open("D:/Python/Data/report.txt", "w", encoding="utf-8") as fout:
            for line in fin:
                name, score = line.strip().split(",")
                grade = "A" if int(score)>=90 else "B" if int(score)>=80 else "C" if int(score)>=70 else "D" if int(score)>=60 else "F"
                print(f"{name}: {score}점({grade})", file=fout)

# ch09_06_2.py
if selected_program == 16 :
    # 카페 매출 분석
    with open("D:/Python/Data/cafe.txt", "w", encoding="utf-8") as f:
        f.write("아메리카노,4500,15\n카페라떼,5000,8\n녹차라떼,5500,12\n")
    total = 0
    with open("D:/Python/Data/cafe.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, price, qty = line.strip().split(",")
            sales = int(price) * int(qty)
            total += sales
            print(f"{name}: {sales:,}원")
    print(f"총 매출: {total:,}원")

# ch09_07_1.py
if selected_program == 17 :
    # try-except 기본구조
    try:
    # 에러가 발생할 수 있는 v\코드
        with open("D:/Python/Data/없는파일.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        # 에러가 발생했을때 실행할 코드
        print("파일을 찾을 수 없습니다!")
    print("프로그램이 계속 실행됩니다!")  # 에러후에도 실행됨

# ch09_07_2.py
if selected_program == 18 :
    # 안전한 파일읽기 함수
    def safe_read(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            print(f"---{filename} 내용---")
            print(content)
            return content
        except FileNotFoundError:
            print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
            return None
    # 안전한 숫자 입력 (while + try-except 조합)
    def safe_int_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("숫자를 입력해주세요!")
    file = safe_read(input("파일 명:"))
    age = safe_int_input("나이: ")  # 숫자 입력할때 까지 반복

# ch09_07_3.py
if selected_program == 19 :
    # 안전한 파일 읽기 프로그램
    def safe_read_file():
        while True:
            filename = input("파일 이름(종료: q): ")
            if filename.lower() == "q":
                break
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    print(f.read())
            except FileNotFoundError:
                print(f"'{filename}' 파일이 없습니다.")
    safe_read_file()
    #존재하는 파일과 없는 파일을 번갈아 입력해보세요!

# my_memo.py
if selected_program == 20:
    FILENAME = "D:/Python/Data/memos.txt"

    def add_memo():
        border = "─" * (WIDTH - 2)
        print("┌" + border + "┐")
        print("│" + vis_center("메모 작성", WIDTH - 2) + "│")
        print("├" + border + "┤")
        print("│" + vis_ljust("  빈 줄 입력 시 저장됩니다.", WIDTH - 2) + "│")
        print("└" + border + "┘")

        lines = []
        while True:
            line = input(" > ")
            if line == "":
                break
            lines.append(line)

        if not lines:
            print("┌" + border + "┐")
            print("│" + vis_center("내용이 없어 저장하지 않았습니다.", WIDTH - 2) + "│")
            print("└" + border + "┘")
            return

        from datetime import datetime
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(f"[{now}]\n")
            for line in lines:
                f.write(f"{line}\n")
            f.write("---\n")

        print("┌" + border + "┐")
        print("│" + vis_center(f"{len(lines)}줄의 메모가 저장되었습니다!", WIDTH - 2) + "│")
        print("└" + border + "┘")

    def show_memos():
        border = "─" * (WIDTH - 2)
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                content = f.read()
            print("┌" + border + "┐")
            print("│" + vis_center("저장된 메모", WIDTH - 2) + "│")
            print("├" + border + "┤")
            if not content.strip():
                print("│" + vis_center("저장된 메모가 없습니다.", WIDTH - 2) + "│")
            else:
                for line in content.splitlines():
                    print("│" + vis_ljust("  " + line, WIDTH - 2) + "│")
            print("└" + border + "┘")
        except FileNotFoundError:
            print("┌" + border + "┐")
            print("│" + vis_center("아직 메모가 없습니다.", WIDTH - 2) + "│")
            print("└" + border + "┘")

    def search_memos():
        border = "─" * (WIDTH - 2)
        print("┌" + border + "┐")
        print("│" + vis_center("메모 검색", WIDTH - 2) + "│")
        print("└" + border + "┘")
        keyword = input(" 검색어: ")

        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                found = [(i+1, line.strip()) for i, line in enumerate(f) if keyword in line]

            print("┌" + border + "┐")
            print("│" + vis_center(f"'{keyword}' 검색 결과: {len(found)}건", WIDTH - 2) + "│")
            print("├" + border + "┤")
            if found:
                for num, text in found:
                    print("│" + vis_ljust(f"  {num}줄: {text}", WIDTH - 2) + "│")
            else:
                print("│" + vis_center(f"'{keyword}'을(를) 찾지 못했습니다.", WIDTH - 2) + "│")
            print("└" + border + "┘")
        except FileNotFoundError:
            print("┌" + border + "┐")
            print("│" + vis_center("메모 파일이 없습니다.", WIDTH - 2) + "│")
            print("└" + border + "┘")

    def clear_memos():
        border = "─" * (WIDTH - 2)
        print("┌" + border + "┐")
        print("│" + vis_center("메모 초기화", WIDTH - 2) + "│")
        print("├" + border + "┤")
        print("│" + vis_center("모든 메모를 삭제합니다. 계속하시겠습니까?", WIDTH - 2) + "│")
        print("└" + border + "┘")
        confirm = input(" (y/n): ").lower()
        if confirm == "y":
            with open(FILENAME, "w", encoding="utf-8") as f:
                pass
            print("┌" + border + "┐")
            print("│" + vis_center("삭제 완료!", WIDTH - 2) + "│")
            print("└" + border + "┘")

    def export_html():
        border = "─" * (WIDTH - 2)
        try:
            with open(FILENAME, "r", encoding="utf-8") as f:
                content = f.read()
            # 메모가 없는 경우 처리
            if not content.strip():
                print("┌" + border + "┐")
                print("│" + vis_center("저장된 메모가 없습니다.", WIDTH - 2) + "│")
                print("└" + border + "┘")
                return

            # 메모 구조 Parsing
            memos = []
            current = {"date": "", "lines": []}
            for line in content.splitlines():
                if line.startswith("[") and line.endswith("]"):
                    if current["lines"]:
                        memos.append(current)
                    current = {"date": line[1:-1], "lines": []}
                elif line == "---":
                    if current["lines"]:
                        memos.append(current)
                    current = {"date": "", "lines": []}
                else:
                    if line:
                        current["lines"].append(line)

            # HTML 파일로 내보내기
            from datetime import datetime
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            html_filename = "D:/Python/Data/memos.html"

            #HTML 템플릿에 메모 내용 넣기
            #템플릿 제작 : 유진혁 
            #제작 날짜 : 2026-01-06
            with open(html_filename, "w", encoding="utf-8") as f:
                print("""<!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>나만의 메모장</title>
        <style>
            :root {
                --bg-color: #f8f9fa;
                --notepad-bg: #ffffff;
                --text-color: #212529;
                --border-color: #dee2e6;
                --btn-bg: #007bff;
                --btn-hover: #0056b3;
            }

            body {
                margin: 0;
                padding: 20px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                display: flex;
                justify-content: center;
                align-items: flex-start;
                min-height: 90vh;
            }

            .container {
                width: 100%;
                max-width: 800px;
                background: var(--notepad-bg);
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                border: 1px solid var(--border-color);
                display: flex;
                flex-direction: column;
                overflow: hidden;
            }

            .toolbar {
                padding: 10px 15px;
                background-color: #f1f3f5;
                border-bottom: 1px solid var(--border-color);
                display: flex;
                gap: 10px;
                align-items: center;
            }

            .status {
                font-size: 13px;
                color: #6c757d;
                margin-left: auto;
            }

            .memo-list {
                padding: 20px;
                display: flex;
                flex-direction: column;
                gap: 16px;
            }

            .memo-card {
                border: 1px solid var(--border-color);
                border-radius: 6px;
                padding: 16px 20px;
                background: #fdfdfd;
            }

            .memo-date {
                font-size: 12px;
                color: #6c757d;
                margin-bottom: 10px;
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 8px;
            }

            .memo-line {
                font-size: 15px;
                color: var(--text-color);
                line-height: 1.8;
            }

            .memo-count {
                font-size: 13px;
                color: #6c757d;
            }
        </style>
    </head>
    <body>
    <div class="container">
        <div class="toolbar">
            <span class="memo-count">총 메모 수: """ + str(len(memos)) + """개</span> 
            <span class="status">내보낸 날짜: """ + now + """</span>
        </div>
        <div class="memo-list">""", file=f)

                for memo in memos:
                    print("        <div class='memo-card'>", file=f)
                    print(f"            <div class='memo-date'>📅 {memo['date']}</div>", file=f)
                    
                    for line in memo["lines"]:
                        print(f"            <div class='memo-line'>{line}</div>", file=f)
                    print("        </div>", file=f)

                print("""    </div>
    </div>
    </body>
    </html>""", file=f)

            print("┌" + border + "┐")
            print("│" + vis_center("HTML 내보내기 완료!", WIDTH - 2) + "│")
            print("├" + border + "┤")
            print("│" + vis_ljust(f"  파일명 : {html_filename}", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  메모 수: {len(memos)}개", WIDTH - 2) + "│")
            print("│" + vis_ljust(f"  날짜   : {now}", WIDTH - 2) + "│")
            print("└" + border + "┘")

        except FileNotFoundError:
            print("┌" + border + "┐")
            print("│" + vis_center("메모 파일이 없습니다.", WIDTH - 2) + "│")
            print("└" + border + "┘")

    def main():
        border = "─" * (WIDTH - 2)
        while True:
            print("┌" + border + "┐")
            print("│" + vis_center("나만의 메모장", WIDTH - 2) + "│")
            print("├" + border + "┤")
            print("│" + vis_ljust("  1. 메모 작성", WIDTH - 2) + "│")
            print("│" + vis_ljust("  2. 메모 보기", WIDTH - 2) + "│")
            print("│" + vis_ljust("  3. 메모 검색", WIDTH - 2) + "│")
            print("│" + vis_ljust("  4. 메모 초기화", WIDTH - 2) + "│")
            print("│" + vis_ljust("  5. HTML 내보내기", WIDTH - 2) + "│")
            print("│" + vis_ljust("  0. 종료", WIDTH - 2) + "│")
            print("└" + border + "┘")
            choice = input(" 선택: ")

            if choice == "1":   add_memo()
            elif choice == "2": show_memos()
            elif choice == "3": search_memos()
            elif choice == "4": clear_memos()
            elif choice == "5": export_html()
            elif choice == "0": break

    main()