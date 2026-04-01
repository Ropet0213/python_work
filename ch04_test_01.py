#=======================================================================
# 파일명 : ch04_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-04-01
#=======================================================================

print(">> 1. sum_n.py")
print(">> 2. gugudan_one.py")
print(">> 3. string_loop.py")
print(">> 4. count_pass.py")
print(">> 5. countdown.py")
print(">> 6. password_limit.py")
print(">> 7. break_find.py")
print(">> 8. continue_example.py")
print(">> 9. prime_check.py")
print(">> 10. menu_loop.py")
print(">> 11. nested_basic.py")
print(">> 12. gugudan_all.py")
print(">> 13. star_triangle.py")
print(">> 14. reversed_triangle.py")
print(">> 15. gugudan_project.py")
selected_program = int(input("실행할 프로그램 번호를 선택하세요 : "))

#sum_n.py
if selected_program == 1:
    n = int(input("1부터 100까지의 합을 구할 숫자를 입력하세요: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print("1부터", n, "까지의 합은", total, "입니다.")

#gugudan_one.py
elif selected_program == 2:
    dan = int(input("출력할 구구단의 단을 입력하세요: "))
    print(f"============================{dan}단============================")
    for i in range(1, 10):
        print(f"{dan:^5} x {i:^5} = {dan * i:^8}")

#string_loop.py
elif selected_program == 3:
    word = "파이썬"
    for char in word:
        print(f"글자 : {char}")

#count_pass.py
elif selected_program == 4:
    scores = [85, 42, 73, 91, 56, 67, 88, 45, 92, 78]
    pass_count = 0
    for score in scores:
        if score >= 60:
            pass_count += 1
    print(f"총 {len(scores)}명 중 {pass_count}명이 합격했습니다.")

#countdown.py
elif selected_program == 5:
    import time
    for i in range(10, 0, -1):
        print(f"\r카운트다운: {i}초", end="")
        time.sleep(1)
    print("\n발사!!!!")

#password_limit.py
elif selected_program == 6: 
    PASSWORD = "python123"
    tries = 0
    max_tries = 3
    while tries < max_tries:
        tries += 1
        pw = input(f"비밀번호({tries}/{max_tries}): ")
        if pw == PASSWORD:
            print("로그인성공!")
            break
        print(f"틀렸습니다. ({max_tries - tries}회남음)")
        if tries >= 2:
            print("힌트 : 비밀번호는 영문소문자와 숫자로 구성되어 있습니다.")
    else:  # break 없이 끝나면
            print(f"{max_tries}회 실패. 계정이 잠겼습니다.")

#break_find.py
elif selected_program == 7:
    numbers = [3, 7, 2, 9, 5, 1, 8, 4]
    target = 5
    for num in numbers:
        if num == target:
            print(f"{target}을 찾았습니다!")
            break    #숫자 발견
        print(f"{num} 확인...", end=" ")

#continue_example.py
elif selected_program == 8:
    for i in range(1, 11):
        if i % 2 == 0:    # 짝수일시
            continue      # 건너뜀
        print(i, end=" ") # 홀수만 출력

#prime_check.py
elif selected_program == 9:
    num = int(input("소수인지 확인할 숫자를 입력하세요: "))
    if num < 2:
        print(f"{num}은 소수가 아닙니다.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num}은 소수가 아닙니다.")
                break
        else:  # break 없이 끝나면
            print(f"{num}은 소수입니다.")

#menu_loop.py
elif selected_program == 10:
    while True:
        print("[1] 인사하기 [2] 계산하기 [3] 종료")
        choice = input("선택: ")
        if choice == "1":
            print("안녕하세요!")
        elif choice == "2":
            a = int(input("숫자 1: "))
            b = int(input("숫자 2: "))
            print(f"{a} + {b} = {a + b}")
        elif choice == "3":
            print("프로그램을 종료합니다.") ; break
        else:
            print("1~3 중에서 선택하세요!")

#nested_basic.py
elif selected_program == 11:
    for i in range(1, 4):    # i: 1, 2, 3
        for j in range(1, 4): # j: 1, 2, 3 (매번처음부터!)
            print(f"i={i}, j={j}", end=" ")
        print()    

#gugudan_all.py
elif selected_program == 12:
    for dan in range(2, 10):       # 바깥: 2~9단
        print(f"==== {dan}단====")
        #===== {dan}단====="
        for i in range(1, 10):     # 안쪽: 1~9
            print(f"{dan} x {i} = {dan * i}")

#star_triangle.py
elif selected_program == 13:
    n = int(input("높이: "))
    for i in range(1, n + 1):  # i: 1 ~ n
        for j in range(i):     # j: 0 ~ i-1 (i개출력)
            print("★", end=" ")
        print()

#reversed_triangle.py
elif selected_program == 14:
    n = int(input("높이: "))
    for i in range(n, 0, -1):  # i: n ~ 1
        for j in range(i):     # j: 0 ~ i-1 (i개출력)
            print("★", end=" ")
        print()

#gugudan_project.py
elif selected_program == 15:
    while True:
        # 메인 메뉴 UI (너비를 40칸으로 고정)
        print("\n" + "┌" + "─" * 38 + "┐")
        print(f"│{'[ 구구단 종합 출력기 ]':^30}│")
        print("├" + "─" * 38 + "┤")
        print(f"│  [1] 특정 단 출력{'':<20}│")
        print(f"│  [2] 범위 지정 출력{'':<18}│")
        print(f"│  [3] 구구단 표 출력{'':<18}│")
        print(f"│  [4] 프로그램 종료{'':<19}│")
        print("└" + "─" * 38 + "┘")
        
        choice = input(" 메뉴 선택 >> ")

        if choice == "4":
            print("\n프로그램을 종료합니다. 안녕~~~")
            break
            
        elif choice == "1":
            dan = int(input(" 출력할 단(2~9) >> "))
            print("\n" + "┌" + "─" * 14 + "┐")
            print(f"│   {dan}단 출력   │")
            print("├" + "─" * 14 + "┤")
            for j in range(1, 10):
                # f-string 정렬을 사용하여 수식 정렬
                print(f"│  {dan} x {j} = {dan * j:>2}  │")
            print("└" + "─" * 14 + "┘")

        elif choice == "2":
            start = int(input(" 시작 단 >> "))
            end = int(input(" 끝 단   >> "))
            
            if start > end:
                print("\n오류: 시작단이 끝단보다 클 수 없습니다.")
                continue
            
            for i in range(start, end + 1):
                print(f"\n▶ {i}단")
                print("-" * 15)
                for j in range(1, 10):
                    print(f" {i} x {j} = {i * j:>2}")
                print("-" * 15)

        elif choice == "3":
            print("\n" + "═" * 66)
            print(f"{'[ 전체 구구단 표 ]':^64}")
            print("═" * 66)
            
            # 헤더 출력
            header = "  x  |" 
            for i in range(2, 10):
                header += f"  {i}단  "
            print(header)
            print("-" * 66)
            
            # 본문 출력
            for j in range(1, 10):
                row = f"  {j}  |"
                for i in range(2, 10):
                    row += f"{i*j:^7}"
                print(row)
            print("═" * 66)
            
        else:
            print("\n[!] 잘못된 입력입니다. 1번부터 4번 사이의 숫자를 입력하세요.")
