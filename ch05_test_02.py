#=======================================================================
# 파일명 : ch05_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-04-08
#=======================================================================

import os

def clear_screen(): #화면 클리어
    os.system('cls' if os.name == 'nt' else 'clear')

def get_vis_width(text): #시각적 너비 계산 알고리즘
    width = 0
    for char in text:
        if ord('가') <= ord(char) <= ord('힣'): # 한글 범위 설정
            width += 2
        else:
            width += 1
    return width

def vis_center(text, total_width): # vis_width 기준으로 중앙정렬
    current = get_vis_width(text)
    padding = (total_width - current) // 2
    return " " * padding + text + " " * (total_width - current - padding) # 공백 * 정렬 * 공백+나머지

def vis_ljust(text, total_width): # vis_width 기준으로 왼쪽정렬
    current = get_vis_width(text)
    return text + " " * (total_width - current)

def caesar(text, shift): #박경호 교수님의 소스 사용
    result = ""
    for char in text:
        if char.isupper():
            new_code = (ord(char) - ord("A") + shift) % 26 + ord("A")
            result += chr(new_code)
        elif char.islower():
            new_code = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result += chr(new_code)
        else:
            result += char
    return result

# 메인 출력 UI
WIDTH = 60 #상자 너비 (되도록 변경 ㄴㄴㄴㄴㄴ)

#초기 화면
clear_screen()
print("┌" + "─" * (WIDTH - 2) + "┐")
print("│" + vis_center("CAESAR CIPHER SYSTEM 2026", WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")
print("│" + vis_ljust("  암호화할 문장을 영어로 입력하세요...", WIDTH - 2) + "│")
print("└" + "─" * (WIDTH - 2) + "┘")

text = input("  >> ")
shift_input = input("  이동할 칸 수: ")
shift = int(shift_input) if shift_input.isdigit() else 0

# 결과 화면
encrypted = caesar(text, shift)

#복호화 알고리즘 구현
decrypted = "" 
for char in encrypted:
    if char.isupper():
        new_code = (ord(char) - ord("A") - shift) % 26 + ord("A") #복호화는 반대로 이동 -shift
        decrypted += chr(new_code)
    elif char.islower():
        new_code = (ord(char) - ord("a") - shift) % 26 + ord("a") #복호화는 반대로 이동
        decrypted += chr(new_code)
    else:
        decrypted += char

#decrypted = caesar(encrypted, -shift) 이것도 사용 가능, 예시로 복호화 알고리즘 구현

clear_screen() # 무조건 화면 클리어하고 시작 
print("┌" + "─" * (WIDTH - 2) + "┐")
print("│" + vis_center("ENCRYPTION RESULT", WIDTH - 2) + "│")
print("├" + "─" * (WIDTH - 2) + "┤")
print(f"│ {vis_ljust('[원본] : ' + text, WIDTH - 4)} │")
print(f"│ {vis_ljust('[암호] : ' + encrypted, WIDTH - 4)} │")
print(f"│ {vis_ljust('[복호] : ' + decrypted, WIDTH - 4)} │")
print("├" + "─" * (WIDTH - 2) + "┤")
print("│" + vis_center("엔터를 누르면 종료됩니다.", WIDTH - 2) + "│")
print("└" + "─" * (WIDTH - 2) + "┘")
input()
