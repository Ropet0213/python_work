#=======================================================================
# 파일명 : ch03_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-03-25 
#=======================================================================
import random

rock = """
    _______
---'   ____)
       (_____)
컴퓨터  (_____)
       (____)
---. __(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
컴퓨터     _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
컴퓨터 __________)
      (____)
---.__(___)
"""

print("=" * 30)
print("안내면 진다 가위바위보!")
print("=" * 30)
print("1. 가위  2. 바위  3. 보 (숫자로 입력)")
user_choice = int(input("가위, 바위, 보 중 하나를 선택하세요: "))
computer_choice = random.randint(1, 3)

if computer_choice == 1:
    print(scissors)
elif computer_choice == 2:
    print(rock)
else:
    print(paper)


if user_choice == computer_choice:
    print("비겼습니다!")
elif (user_choice == 1 and computer_choice == 3) or \
     (user_choice == 2 and computer_choice == 1) or \
     (user_choice == 3 and computer_choice == 2):
    print("이겼습니다!")
else:
    print("졌습니다!")
