#=======================================================================
# 파일명 : ch04_test_02.py
# 작성자 : 유진혁
# 작성일 : 2026-04-01
#=======================================================================

print("정삼각형 그리기")
print("------------------------------------")
height = int(input("삼각형의 높이를 입력하세요: "))

for i in range(1, height + 1):
    blank = " " * (height - i) # 공백 계산
    stars = "★ " * i # 별 계산
    print(blank + stars)

print("=" * 40)
print("다이아몬드 그리기")
print("------------------------------------")
height = int(input("다이아몬드의 높이를 입력하세요 (홀수): "))
if height % 2 == 0:
    print("홀수를 입력해주세요!")
else:
    mid = height // 2 + 1
    for i in range(1, mid + 1): # 1 ~ mid
        blank = " " * (mid - i)
        stars = "★ " * i
        print(blank + stars)
    for i in range(mid - 1, 0, -1): # mid-1 ~ 1
        blank = " " * (mid - i)
        stars = "★ " * i
        print(blank + stars)

print("마름모 그리기")
print("------------------------------------")
size = int(input("마름모의 크기를 입력하세요: "))
for i in range(size): # 0 ~ size-1
    print(" " * (size - i) + "★ " * size)
