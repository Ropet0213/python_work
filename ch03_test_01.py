#=======================================================================
# 파일명 : ch03_test_01.py
# 작성자 : 유진혁
# 작성일 : 2026-03-25 
#=======================================================================

#코딩 프로그램 구분하는 함수 선언
def print_line():
    print("-" * 30)

alphabet_Aplus = """
   ░███            
  ░██░██           
 ░██  ░██    ░██   
░█████████ ░██████ 
░██    ░██   ░██   
░██    ░██         
░██    ░██  
"""

alphabet_a = """
   ░███    
  ░██░██   
 ░██  ░██  
░█████████ 
░██    ░██ 
░██    ░██ 
░██    ░██
"""

alphabet_Bplus = """
░████████           
░██    ░██          
░██    ░██    ░██   
░████████   ░██████ 
░██     ░██   ░██   
░██     ░██         
░█████████          
"""

alphabet_b = """
░████████   
░██    ░██  
░██    ░██  
░████████   
░██     ░██ 
░██     ░██ 
░█████████  
"""

alphabet_c = """
  ░██████  
 ░██   ░██ 
░██        
░██        
░██        
 ░██   ░██ 
  ░██████  
"""
alphabet_d = """
░███████   
░██   ░██  
░██    ░██ 
░██    ░██ 
░██    ░██ 
░██   ░██  
░███████   
"""

alphabet_f = """
░██████████
░██        
░██        
░█████████ 
░██        
░██        
░██        
"""

print("\n>>>> D:\Python\Python_Study\Week4")
print(">> hello.py")
print(">> greeting_v2.py")
print(">> check_positive.py")
print(">> check_number.py")
print(">> even_odd.py")
print(">> pass_fail.py")
print(">> grade.py")
print(">> scholarship.py")
print(">> ride.py")
print(">> library.py")
print(">> theme_park.py")
print(">> member_discount.py")
print(">> grade_checker.py")

program_name = input("\n Select program to run: ")

#hello.py
if program_name == "hello.py":
    name4 = input("이름을 입력하세요: ")
    print(f"안녕하세요, {name4}님!")
    print(f"{name4}님의 이름은{len(name4)}글자입니다.")

#greeting_v2.py
elif program_name == "greeting_v2.py":
    name8 = input("이름: ")
    hour = int(input("현재시간(0~23): "))
    if hour < 12:   # 오전
        print(f"좋은 아침이에요, {name8}님!")
    else:            # 오후
        print(f"안녕하세요, {name8}님!")

#check_positive.py
elif program_name == "check_positive.py":
    number = int(input("숫자를 입력하세요: "))
    if number > 0:    # 조건문을 이용하여 양수인지 확인
        print(f"{number}은(는) 양수입니다!")
        print("프로그램을 종료합니다.")  

#check_number.py
elif program_name == "check_number.py":
    number1 = int(input("숫자: "))
    if number1 > 0:
        print(f"{number1}은(는) 양수입니다!")
    elif number1 < 0:
        print(f"{number1}은(는) 음수입니다!")
    else :
        print(f"{number1}은(는) 0입니다!")

    print("프로그램 끝")

#even_odd.py
elif program_name == "even_odd.py":
    number13 = int(input("정수를 하나 입력하세요: "))
    if number13 % 2 == 0:
        print(f"{number13}은(는) 짝수입니다.")
    else:
        print(f"{number13}은(는) 홀수입니다.")

#pass_fail.py
elif program_name == "pass_fail.py":
    score13 = int(input("시험점수를입력하세요: "))
    if score13 >= 60:
        print("축하합니다! 합격입니다.")
        print(f"당신의 점수: {score13}점")
    else:
        print("아쉽지만 불합격입니다.")
        print(f"합격까지{60 -score13}점부족합니다.")

#grade.py
elif program_name == "grade.py":
    score16 = int(input("점수: "))
    if score16 >= 95:
        grade16 = "A+"
    elif score16 >= 90:
        grade16 = "A"
    elif score16 >= 85:
        grade16 = "B+"
    elif score16 >= 80:
        grade16 = "B"
    elif score16 >= 70:
        grade16 = "C"
    elif score16 >= 60:
        grade16 = "D"
    else:
        grade16 = "F"
    print(f"당신의 등급: {grade16}")

#scholarship.py
elif program_name == "scholarship.py":
    gpa = float(input("학점(0.0~4.5): "))
    if gpa >= 4.0:
        print("최우수 장학금 대상입니다!")
    elif gpa >= 3.5:
        print("우수 장학금 대상입니다!")
    elif gpa >= 3.0:
        print("일반 장학금 대상입니다!")
    else:
        print("장학금 대상이 아닙니다.")

#ride.py
elif program_name == "ride.py":
    height21 = int(input("키(cm): "))
    age21 = int(input("나이: ")) 
    if height21 >= 130 and age21 >= 7:
        print("탑승 가능합니다!")
    else:
        print("탑승조건을 충족하지 못합니다.")

    if age21 >= 65 or age21 <= 18:
        print("할인적용!")

#교안 22쪽 손코딩
#나이와 회원 유무 입력받기
elif program_name == "library.py":
    age22 = int(input("나이: "))
    Check_member22 = int(input("비회원은 0번, 회원은 1번, 직원은 2번을 눌러주세요. : "))

    #전자책 열람 가능 여부 판단
    if age22 >= 19 and Check_member22 == 1:
        print("전자책 열람 가능!")
    elif age22 >= 19 and Check_member22 == 2:
        password22 = input("직원 비밀번호를 입력해주세요: ")
        if password22 == "admin123":
            print("모든 전자책 열람 가능!")
        else:
            print("비밀번호가 틀렸습니다. 프로그램을 다시 실행해주세요.")
    else:
        print("비회원은 로그인 후 이용해주세요.")

#theme_park.py
elif program_name == "theme_park.py":
    print("소숫점을 제외하여 반올림해서 입력해주세요.")
    height26 = int(input("키(cm): "))

    if height26 >= 120: #키가 120cm 이상인지 확인
        print("키가 충분합니다. 나이를 입력해주세요.")
        age26 = int(input("나이: "))

        if age26 >= 5: #나이가 5세 이상인지 확인
            print("탑승 가능합니다!")

        else:
            print("나이가 부족합니다.")
            is_guardian26 = input("보호자가 있나요? (yes/no): ")

            if is_guardian26.lower() == "yes": #보호자가 있는지 확인
                print("보호자가 있으므로 탑승 가능합니다. 반드시 보호자와 함께 탑승해주세요!")

            else:
                print("보호자가 없으므로 탑승이 불가능합니다.")

    else: 
        print("키가 부족합니다. 탑승이 불가능합니다.")

#member_discount.py
elif program_name == "member_discount.py":
    price25 = int(input("상품가격: "))
    is_member25 = input("회원이세요? (yes/no): ")
    if is_member25 == "yes":
        grade25 = input("회원등급(VIP/일반): ")
        if grade25 == "VIP":
            discount25 = 0.2
            print("VIP 회원20% 할인!")
        else:
            discount25 = 0.1
            print("일반회원10% 할인!")
            print(f"결제금액: {int(price25 * (1 -discount25))}원")
    else:
        print(f"비회원정상가: {price25}원")



#성적 등급 판별기

elif program_name == "grade_checker.py":
    print("=" * 30)
    print("성적 등급 판별기에 오신것을 환영합니다.")
    print("=" * 30)
    name = input("이름을 입력하세요: ")
    score = float(input("점수를 입력하세요 (80점 만점): "))
    check_absent = int(input("결석 일수를 입력하세요. 미결석시 0을 입력하세요: "))

    attendance_score = 30 - check_absent * 5
    total_score = score + attendance_score

    if total_score >= 96:
        grade = "A+"
        print(alphabet_Aplus)
    elif total_score >= 90:
        grade = "A"
        print(alphabet_a)
    elif total_score >= 85:
        grade = "B+"
        print(alphabet_Bplus)
    elif total_score >= 80:
        grade = "B"
        print(alphabet_b)
    elif total_score >= 70:
        grade = "C"
        print(alphabet_c)
    elif total_score >= 60:
        grade = "D"
        print(alphabet_d)
    else:
        grade = "F"
        print(alphabet_f)

    print(f"이름 : {name} // 등급 : {grade} // 점수 : {total_score:.1f}점")
    print("=" * 30)
    print("평가 세부사항: ")
    if total_score >= 96:
        print("훌륭합니다! A+ 등급을 받으셨습니다. 출석 점수와 시험 점수가 남들보다 월등히 높습니다. 장학금 걱정은 없겠네요!")
    elif total_score >= 90:
        if check_absent == 0:
            print("좋습니다! A 등급을 받으셨습니다. 출석 점수와 시험 점수가 모두 우수하여 높은 등급을 받으셨습니다. 앞으로도 꾸준히 노력해주세요!")
        else:
            print("좋습니다! A 등급을 받으셨습니다. 시험 점수는 우수하지만 출석 점수가 조금 아쉽네요. 다음 학기에는 결석을 줄여서 A+ 등급을 노려봅시다!")
    elif total_score >= 85:
        if check_absent == 0:
            print("잘하셨습니다! B+ 등급을 받으셨습니다. 출석 점수와 시험 점수가 매우 좋습니다. 조금만 더 열심히 노력해서 A를 노려봅시다!")
        else:
            print("잘하셨습니다! B+ 등급을 받으셨습니다. 시험 점수는 우수하지만 출석 점수가 조금 아쉽네요. 다음 학기에는 결석을 줄여볼까요?")
    elif total_score >= 80:
        if check_absent == 0:
            print("괜찮습니다! B 등급을 받으셨습니다. 출석 점수와 시험 점수가 좋습니다. 무난하네요. 수고하셨습니다.")
        else:
            print("B 등급을 받으셨습니다. 시험 점수는 좋았는데 출석 점수가 아쉬워요. 다음 학기에는 결석을 줄여볼까요?")
    elif total_score >= 70:
        if check_absent == 0:
            print("괜찮습니다! C 등급을 받으셨습니다. 출석 점수는 좋지만 시험 점수가 조금 아쉽네요. 다음 학기에는 시험 점수를 좀 더 올려보도록 노력해봅시다!")
        else:
            print("C 등급을 받으셨습니다. 출석 점수와 시험 점수가 보통입니다. 수고하셨습니다.")
    elif total_score >= 60:
        print("D 등급을 받으셨습니다. 출석 점수와 시험 점수가 낮습니다. 조금 더 노력해주세요. 아니, 더 많이 노력해주세요.")
    else:
        print("안타깝게도 F 등급을 받으셨습니다. 재수강 확정이네요. 다음 학기에 봐요~")

