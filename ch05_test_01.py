#=======================================================================
# 파일명 : ch05_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-04-08
#=======================================================================

print("┌" + "─" * 66 + "┐")
print("│" + "PYTHON CHAPTER 05 TEST SYSTEM".center(66) + "│")
print("├" + "─" * 66 + "┤")
print("│ 1.ch05_01_1    2.ch05_01_2   3.ch05_01_3   4.ch05_02_1           │")
print("│ 5.slicing_demo 6.ch05_02_2   7.ch05_02_3   8.ch05_03_1           │")
print("│ 9.ch05_03_2    10.ch05_04_1  11.ch05_04_2  12.ch05_04_3          │")
print("│ 13.ch05_04_4   14.ch05_04_5  15.ch05_04_6  16.ch05_05_1          │")
print("│ 17.ch05_05_2   18.ch05_05_3  19.ch05_05_4  20.ch05_05_5          │")
print("│ 21.ch05_06_1   22.ch05_06_2  23.ch05_06_3  24.ch05_06_5          │")
print("│ 25.ch05_07_1                                                     │")
print("├" + "─" * 66 + "┤")
print("│        실행할 프로그램 번호를 입력하세요 (1~25)                  │")
print("└" + "─" * 66 + "┘")

selected_program = int(input(">> "))


#ch05_01_1.py
if selected_program == 1:
    word = "Python"
    print(word[0])   # P (첫번째 글자)
    print(word[-1])  # n (마지막 글자)
    print(word[-2])  # o (끝에서 두번째)
    # len() — 문자열 길이
    print(len(word)) # 6
    # 마지막 인덱스= len() -1 = 5

#ch05_01_2.py
elif selected_program == 2:
    word = "파이썬"
    for i in range(len(word)):
        print(f"인덱스{i}: {word[i]}")

#ch05_01_3.py
elif selected_program == 3:
    name = input("이름을입력하세요: ")
    print(f"첫 글자: {name[0]}")
    print(f"마지막글자: {name[-1]}")
    print(f"글자수: {len(name)}자")

#ch05_02_1.py
elif selected_program == 4:
    word = "Python"
    print(word[0:3])  # Pyt (0,1,2번 글자)
    print(word[2:5])  # tho
    print(word[:3])   # Pyt (처음 ~ 2번)
    print(word[3:])   # hon (3번 ~ 끝)
    print(word[:])    # Python (전체)
    print(word[::2])  # Pto (2칸씩 건너뜀)
    print(word[::-1]) # nohtyP (뒤집기!)


#slicing_demo.py
elif selected_program == 5:
    import time

    text = "  Welcome to Lotte World!  "
    disp_width = 30  # 전광판의 가로 너비
    pad = " " * disp_width
    full_text = pad + text + pad

    print("┌" + "─" * (disp_width) + "┐")

    try:
        while True:
            for i in range(len(full_text) - disp_width):
                # 흐르는 효과
                scroll = full_text[i : i + disp_width]
                print(f"\r│{scroll}│", end="", flush=True)
            
                time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n└" + "─" * (disp_width) + "┘")
        print("전광판을 종료합니다.")   


#ch05_02_2.py
elif selected_program == 6:
    # 파일확장자 추출
    filename = "report_2024.pdf"
    ext  = filename[-3:]   # pdf
    name = filename[:-4]   # report_2024
    print(f"파일명: {name}, 확장자: {ext}")
    # 날짜 문자열 분해
    date  = "2024-03-15"
    year  = date[:4]       # 2024
    month = date[5:7]      # 03
    day   = date[8:]       # 15
    print(f"년: {year}, 월: {month}, 일: {day}")

#ch05_02_3.py
elif selected_program == 7:
    word = input("단어를 입력하세요: ").strip() # 양쪽 공백 제거
    reversed_word = word[::-1]
    print(f"뒤집으면: {reversed_word}")
    if word == reversed_word:
        print("회문 입니다! ")
    else:
        print("회문이 아닙니다. ")

#ch05_03_1.py
elif selected_program == 8:
    word = "Hello"
    # 방법 1: 슬라이싱으로 새 문자열 조합
    new_word = "J" + word[1:]  # 'J' + 'ello'
    print(new_word)  # Jello
    # 방법 2: replace() 메서드
    new_word2 = word.replace("H", "J")
    print(new_word2)  # Jello
    # 원본은 변하지 않음
    print(word)  # Hello

#ch05_03_2.py
elif selected_program == 9:
    word = "hello"
    word.upper()       # 'HELLO'를 반환하지만 word는 그대로
    print(word)        # hello (원본 그대로!)
    word = word.upper() # 이렇게 재할당해야 word가 바뀜!
    print(word)         # HELLO

#ch05_04_1.py
elif selected_program == 10:
    msg = "hello python"
    print(msg.upper())      # HELLO PYTHON
    print(msg.lower())      # hello python
    print(msg.capitalize()) # Hello python (첫 글자만 대문자)
    print(msg.title())      # Hello Python (각 단어 첫글자)
    print(msg.swapcase())   # HELLO PYTHON → 대소문자 뒤바꿈

#ch05_04_2.py
elif selected_program == 11:
    name = "  홍길동"
    print(name.strip())   # '홍길동' (앞 뒤 모두 제거)
    print(name.lstrip())  # '홍길동' (왼쪽만)
    print(name.rstrip())  # '  홍길동' (오른쪽만)
    # 실전: 입력과 strip()은 짝꿍!
    name = input("이름: ").strip()
    print(f"안녕하세요, {name}님!")

#ch05_04_3.py
elif selected_program == 12:
    sentence = "파이썬은 재미있고 파이썬은 강력하다"
    print(sentence.find("파이썬"))   # 0 (첫 등장 위치)
    print(sentence.find("자바"))     # -1 (없으면 -1)
    print(sentence.count("파이썬"))  # 2 (몇 번 나오나)
    filename = "report_2024.pdf"
    print(filename.startswith("report")) # True
    print(filename.endswith(".pdf"))     # True

#ch05_04_4.py
elif selected_program == 13:
    # replace(바꿀것, 새것, 횟수)
    msg = "사과는맛있다. 사과는빨갛다."
    print(msg.replace("사과", "바나나"))    # 전부 교체
    print(msg.replace("사과", "바나나", 1)) # 1번만 교체
    # split() — 쪼개기→ 리스트 반환
    csv = "사과,바나나,포도"
    fruits = csv.split(",")   # ['사과', '바나나', '포도’]
    print(fruits)
    # join() — 합치기 ← split()의 반대
    result = " / ".join(fruits) # 사과/ 바나나/ 포도
    print(result)

#ch05_04_5.py
elif selected_program == 14:
    #ch05_04_5.py
    name = input("이름을 입력해주세요 : ").strip().capitalize()
    print(f"정제된 이름: {name}")

#ch05_04_6.py
elif selected_program == 15:
    data = "홍길동, 20, 서울"
    parts = data.split(",")
    print(f"이름: {parts[0]}, 나이: {parts[1]}, 도시:{parts[2]}")


#ch05_05_1.py
elif selected_program == 16:
    text = input("영어 문장을 입력하세요: ").strip() #공백 제거
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:  # in 연산자로 포함 여부 확인
            count += 1
    print(f"모음 개수 : {count}개")

#ch05_05_2.py
elif selected_program == 17:
    text = "전화 번호: 010-1234-5678"
    digits = ""
    for char in text:
        if char.isdigit():  # 숫자면 True
            digits += char
    print(f"숫자만: {digits}")  # 01012345678

#ch05_05_3.py
elif selected_program == 18:
    text = "Beautiful Python" # 예시 문장
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char
    print(result)  # B***t*f*l Pyth*n

#ch05_05_4.py
elif selected_program == 19:
    sentence = "I love Python programming"
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    result = " ".join(reversed_words)
    print(result)  # I evol nohtyP gnimmargorp

#ch05_05_5.py
elif selected_program == 20:
    password = input("비밀번호: ")
    has_upper   = any(c.isupper() for c in password)
    has_lower   = any(c.islower() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)  #특수 문자
    score = sum([len(password)>=8, has_upper, has_lower, has_digit, has_special])
    print(f"강도 점수: {score}/5")

#ch05_06_1.py
elif selected_program == 21:
    receipt = "===== 영수증=====\n상품: 아메리카노\n단가: 4,500원\n합계: 9,000원"
    print(receipt)

#ch05_06_2.py
elif selected_program == 22:
    print("이름\t나이\t도시")
    print("홍길동\t20\t서울")
    # Windows 파일 경로(역슬래시 두번)
    print("C:\\Users\\Documents\\파일.txt")

#ch05_06_3.py & ch05_06_4.py
elif selected_program == 23:
    # 방법1: 다른 종류의 따옴표로 감싸기
    print("It's a beautiful day")
    # 방법2: 이스케이프 문자
    print('It\'s a beautiful day')
    # 방법3: 삼중 따옴표(여러줄 문자열에도 유용!)
    print('''It's a "beautiful" day''')
    print(r"C:\new_folder\test")

#ch05_06_5.py
elif selected_program == 24:
    name  = input("이름: ")
    phone = input("전화: ")
    print(f"\n╔══════════════════╗\n║ 이름:\t{name}\n║ 전화:\t{phone}\n╚══════════════════╝")

#ch05_07_1,py & ch05_07_2.py
elif selected_program == 25:
    print(ord("A"))  # 65 (A의유니코드번호)
    print(ord("a"))  # 97
    print(chr(65))   # 'A' (번호→ 글자)
    print(chr(68))   # 'D' (65 + 3)

    char = "Z"
    shift = 3
    new_code = (ord(char) -ord("A") + shift) % 26 + ord("A")
    print(chr(new_code))  # C (Z→A→B→C)

else:
    print("잘못된 번호입니다. 1~25 사이의 번호를 입력해주세요.")