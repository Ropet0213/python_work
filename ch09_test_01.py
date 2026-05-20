#=======================================================================
# 파일명 : ch09_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-05-20
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
WIDTH = 60

clear_screen()
border = "─" * (WIDTH - 2)
print("┌" + border + "┐")
print("│" + vis_center("프로그램 목록", WIDTH - 2) + "│")
print("├" + border + "┤")
print("│" + vis_ljust("  1. ch09_file_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  2. ch09_file_2.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  3. ch09_file_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  4. ch09_file_4.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  5. ch09_file_5_1.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  6. ch09_file_5_2.py ", WIDTH - 2) + "│")
print("│" + vis_ljust("  7. ch09_file_5_3.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  8. ch09_file_6.py", WIDTH - 2) + "│")
print("│" + vis_ljust("  9. ch09_file_7.py", WIDTH - 2) + "│")
print("│" + vis_ljust(" 10. ch09_file_8.py", WIDTH - 2) + "│")
print("└" + border + "┘")
print()
selected_program = int(input("실행할 프로그램 입력 : "))

# ch09_file_1.py
if selected_program == 1 :
    ##동일한 디렉터리에서 새 파일 생성 프로그램##
    print("=" * 55)
    print("■ 동일한 디렉터리에서 새 파일 생성 프로그램")
    print("-" * 55)
    print(" >> 생성할 파일명: writefile.txt ")
    print("-" * 55)
    fileName = open("D:/Python/Data/writefile.txt", "w", encoding="utf-8")
    fileName.close( )
    print("\n   <<<<<  파일 생성 완료  >>>>>   \n")
    print("-" * 55)
    print(" >> 새롭게 생성된 파일이 존재하는지를 확인하세요...")
    print("=" * 55)

#ch09_file_2.py
if selected_program == 2 :
    #다양한 경로 표기 방법
    open("D:/Python/Data/pathfile.txt", "w", encoding="utf-8")    # 슬래시(/) 권장
    open("D:\\Python\\Data\\pathfile.txt", "w")  # 역슬래시는 두번
    # open("./data/result.txt", "w")             # 일단 에러나서 주석 처리

# ch09_file_3.py
if selected_program == 3 :
    ## 다른 디렉터리에 새 파일 생성 프로그램 ##
    print("=" * 55)
    print("■ 다른 디렉터리에 새 파일 생성 프로그램")
    print("-" * 55)
    print(" >> 생성할 파일명: pathfile.txt ")
    print(" >> 생성할 경로명: D:/Python/Data/ ")
    print("-" * 55)
    fileName = open("D:/Python/Data/pathfile.txt", "w", encoding="utf-8") #에러가 나는걸 방지하기 위해서 utf-8 인코딩 설정
    fileName.close( )
    print("\n   <<<<<  파일 생성 완료  >>>>>   \n")
    print("-" * 55)
    print(" >> 새롭게 생성된 파일이 존재하는지를 확인하세요...")
    print("=" * 55)

# ch09_file_4.py
if selected_program == 4 :
    ## 다른 디렉터리에 있는 파일 열기와 쓰기 프로그램 ##
    print("=" * 55)
    print("■ 다른 디렉터리에 있는 파일 열기와 쓰기 프로그램")
    print("-" * 55)
    print(" >> 생성할 파일명: pathfile.txt ")
    print(" >> 생성할 경로명: D:/Python/Data/ ")
    print("-" * 55)
    fileName = open("D:/Python/Data/pathfile.txt", "w", encoding="utf-8") 

    for cnt in range(1, 11) :
        prt = " >> %02d회 동계올림픽\n" % cnt
        fileName.write(prt)

    fileName.close( )

    print("\n   <<<<<  파일 쓰기 완료  >>>>>   \n")
    print("-" * 55)
    print(" >> D:/Python/Data/pathfile.txt 파일의 내용을 확인하세요...")
    print("=" * 55)

# ch09_file_5_1.py
if selected_program == 5 :
    ## 파일 내용 한 행만 읽어오는 프로그램 ##
    print("=" * 55)
    print("■ 파일 내용 한 행만 읽어오는 프로그램")
    print("-" * 55)
    print(" >> 읽어올 파일명: pathfile.txt ")
    print(" >> 대상 파일 경로: D:/Python/Data/ ")
    print("-" * 55)
    print(" >> readline( ) 함수로 파일 내용중 한 행만 읽어옴")
    print("-" * 55)
    print("")
    fileName = open("D:/Python/Data/pathfile.txt", "r", encoding="utf-8")
    first = fileName.readline( )
    print(first)
    fileName.close( )
    print("-" * 55)
    print(" >> 프로그램을 종료합니다...")
    print("=" * 55)

# ch09_file_5_2.py
if selected_program == 6 :
    ## 파일 내용 모든 줄을 리스트로 읽어오는 프로그램 ##
    print("=" * 55)
    print("■ 파일 내용 모든 줄을 리스트로 읽어오는 프로그램")
    print("-" * 55)
    print(" >> 읽어올 파일명: pathfile.txt ")
    print(" >> 대상 파일 경로: D:/Python/Data/ ")
    print("-" * 55)
    print(" >> readlines( ) 함수로 파일 내용 모든 줄을 리스트로 읽어옴")
    print("-" * 55)
    print("")
    fileName = open("D:/Python/Data/pathfile.txt", "r", encoding="utf-8")
    first = fileName.readlines( )
    print(first)
    fileName.close( )
    print("-" * 55)
    print(" >> 프로그램을 종료합니다...")
    print("=" * 55)

# ch09_file_5_3.py
if selected_program == 7 :
    ## 파일 전체 내용 문자열로 읽어오는 프로그램 ##
    print("="* 55)
    print("■ 파일 전체 내용 문자열로 읽어오는 프로그램")
    print("-"* 55)
    print(">> 읽어올 파일명: pathfile.txt ")
    print(">> 대상 파일 경로: D:/Python/Data/ ")
    print("-"* 55)
    print(">> read( ) 함수로 파일 전체 내용을 문자열로 읽어옴")
    print("-" * 55)
    print("")
    fileName = open("D:/Python/Data/pathfile.txt", "r", encoding="utf-8")
    first = fileName.read( )
    print(first)
    fileName.close( )
    print("-" * 55)
    print(" >> 프로그램을 종료합니다...")
    print("=" * 55)

# ch09_file_6.py
if selected_program == 8 :
    ## 파일 내용의 모든 행을 읽어오는 프로그램 ##
    print("=" * 55)
    print("■ 파일 내용의 모든 행을 읽어오는 프로그램")
    print("-" * 55)
    print(" >> 읽어올 파일명: pathfile.txt ")
    print(" >> 대상 파일 경로: D:/Python/Data/ ")
    print("-" * 55)
    print(" >> readlines( ) 함수로 파일 내용의 모든 행을 읽어옴")
    print("-" * 55)

    fileName = open("D:/Python/Data/pathfile.txt", "r", encoding="utf-8")
    allLine = fileName.readlines( )

    for cnt in allLine :
        print(cnt)

    fileName.close( )

    print("-" * 55)
    print(" >> 프로그램을 종료합니다...")
    print("=" * 55)

# ch09_file_7.py
if selected_program == 9 :
    ## 파일에 새로운 내용을 추가하는 프로그램 ##
    print("=" * 55)
    print("■ 파일에 새로운 내용을 추가하는 프로그램")
    print("-" * 55)
    print(" >> 읽어올 파일명: pathfile.txt ")
    print(" >> 대상 파일 경로: D:/Python/Data/ ")
    print("-" * 55)
    print(" >> write( ) 함수로 파일에 새로운 내용 추가하기")
    print("-" * 55)
    print("\n   <<<<<  내용이 추가되었습니다.   >>>>>   \n")

    fileName = open("D:/Python/Data/pathfile.txt", "a", encoding="utf-8")

    data = "---<< 추가 내용 >>---\n"
    fileName.write(data)

    for cnt in range(11, 16) :
        addWrite = " >> %02d 회 동계올림픽 \n" % cnt
        fileName.write(addWrite)

    fileName.close( )

#ch09_file_8.py
if selected_program == 10 :
    ## with~as문으로 파일에 새로운 내용을 추가하는 프로그램 ##
    print("=" * 55)
    print("■with~as 문으로 새로운 내용을 추가하는 프로그램")
    print("-" * 55)
    print(" >> 읽어올 파일명: pathfile.txt ")
    print(" >> 대상 파일 경로: D:/Python/Data/ ")
    print("-" * 55)
    print(" >> with~as 문으로 파일에 새로운 내용 추가하기")
    print("-" * 55)
    print("\n   <<<<<  새로운 내용이 추가되었습니다.   >>>>>   \n")
    # with~as 핵심블록 — close()는 자동으로 호출됨!
    with open("D:/Python/Data/pathfile.txt", "a", encoding="utf-8") as fileName :
        data = "\n---<< 추가내용2 >>---\n"
        fileName.write(data)
        for cnt in range(16, 21) :
            addWrite = f" >> {cnt:02d} 회 동계올림픽\n"
            fileName.write(addWrite)

    print("-" * 55)
    print(" >> D:/Python/Data/pathfile.txt 파일을 열어서 확인하세요.")
    print("-" * 55)
    print(" >> 프로그램을 종료합니다...")
    print("=" * 55)
