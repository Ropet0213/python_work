#=======================================================================
# 파일명 : ch06_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-04-29
#=======================================================================

# 항상 넣는 코드들 (화면 초기화, 시각적 너비 계산, 시각적 정렬)
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

WIDTH = 60 # 상황에 따라서는 변경해도 되지 않을까라는 안일한 생각

grades = [[85,90,78],[92,88,95],[76,82,89]]
names  = ['김철수','이영희','박민수']
subjects = ['국어', '수학', '영어']

# 최고점 학생 계산
max_score = 0
best_student = ""
for i in range(len(grades)):
    for score in grades[i]:
        if score > max_score:
            max_score = score
            best_student = names[i]

clear_screen()

# 타이틀
print("┌" + "─" * (WIDTH - 2) + "┐")
print("│" + vis_center("학생 성적 현황", WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")

# 헤더
header = vis_ljust("  이름", 10) + "".join(vis_center(s, 8) for s in subjects) + vis_center("평균", 10)
print("│" + vis_ljust(header, WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")

# 학생별 점수
for i in range(len(names)):
    avg = sum(grades[i]) / len(grades[i])
    row = vis_ljust(f"  {names[i]}", 10)
    for score in grades[i]:
        row += vis_center(str(score), 8)
    row += vis_center(f"{avg:.1f}", 10)
    print("│" + vis_ljust(row, WIDTH - 2) + "│")

# 최고점 학생
print("├" + "─" * (WIDTH - 2) + "┤")
print("│" + vis_ljust(f"   전체 최고점: {best_student} ({max_score}점)", WIDTH - 2) + "│")
print("└" + "─" * (WIDTH - 2) + "┘")

