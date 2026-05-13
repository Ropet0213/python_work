#=======================================================================
# 파일명 : ch07_test_01.py
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
print("│" + vis_ljust("  1.ch07_tp_1    2.ch07_tp_2    3.ch07_tp_3", WIDTH - 2) + "│")
print("│" + vis_ljust("  4.ch07_tp_4    5.ch07_tp_5    6.ch07_dic_1", WIDTH - 2) + "│")
print("│" + vis_ljust("  7.ch07_dic_2   8.ch07_dic_3   9.ch07_dic_4", WIDTH - 2) + "│")
print("│" + vis_ljust(" 10.ch07_dic_5  11.ch07_dic_6  12.ch07_dic_7", WIDTH - 2) + "│")
print("│" + vis_ljust(" 13.ch07_dic_8  14.ch07_dic_9  15.ch07_dic_11", WIDTH - 2) + "│")
print("│" + vis_ljust(" 16.ch07_dic_12 17.ch07_dic_13 18.ch07_dic_14", WIDTH - 2) + "│")
print("│" + vis_ljust(" 19.ch07_dic_16 20.ch07_dic_18 21.ch07_dic_19", WIDTH - 2) + "│")
print("│" + vis_ljust(" 22.ch07_dic_21 23.ch07_set_1  24.ch07_set_3", WIDTH - 2) + "│")
print("│" + vis_ljust(" 25.ch07_set_4  26.ch07_set_6  27.ch07_set_7", WIDTH - 2) + "│")
print("│" + vis_ljust(" 28.ch07_set_10 29.ch07_set_11 30.ch07_set_12", WIDTH - 2) + "│")
print("└" + border + "┘")

selected_program = int(input("프로그램 번호를 입력하세요: "))

#ch07_tp_1.py
if selected_program == 1:
    # 다양한 튜플 선언 방법
    tp1 = ()                              # 빈 튜플
    tp2 = (101,)                          # 요소 1개 선언시 반드시 콤마 필수
    tp3 = (101, 102, 103)
    tp4 = 201, 202, 203                   # 소괄호없이 선언도 가능
    tp5 = ('one', 'two', 'three')
    print(tp1); print(tp2); print(tp3); print(tp4); print(tp5)

# ch07_tp_2.py
if selected_program == 2:
    # 튜플 인덱싱 예제
    tp = (101, 102, 'one', 'two')
    print(tp[0])     # 첫번째 요소
    print(tp[2])     # 세번째 요소

# ch07_tp_3.py
if selected_program == 3:
    # 튜플 슬라이싱 예제
    tp = (101, 102, 'one', 'two')
    print(tp[2:])    # 세번째부터 마지막까지
    print(tp[1:2])   # 두번째 요소만

# ch07_tp_4.py
if selected_program == 4:
    # 튜플 덧셈 연산
    tp1 = (101, 102)
    tp2 = ('one', 'two')
    print(tp1 + tp2)

# ch07_tp_5.py
if selected_program == 5:
    # 튜플 곱셈 연산
    tp = ('space', 'zone')
    print(tp * 2)
    # 요소 1개 튜플도 가능(콤마 필수!)
    tp = ('Good',)
    print(tp * 5)

# ch07_dic_1.py
if selected_program == 6:
    import base64

    #간단한 비밀번호 암호화 함수, 실전에서는 절대 사용하면 안됨 (단방향해시 사용 권장)
    def encrypt_password(password):
        #비밀번호 암호화 (Base64 + 간단한 XOR)
        key = 42
        encrypted = ''.join(chr(ord(c) ^ key) for c in password)
        #Base64로 인코딩하여 저장
        return base64.b64encode(encrypted.encode()).decode()

    def decrypt_password(encrypted):
        #비밀번호 복호화
        key = 42
        #Base64 디코딩
        decoded = base64.b64decode(encrypted.encode()).decode()
        #XOR 복호화
        return ''.join(chr(ord(c) ^ key) for c in decoded)

    # 비밀번호 암호화해서 저장
    encrypted_passwd = encrypt_password('123456')
    d1 = {'id':'cskisa', 'passwd':encrypted_passwd, 'email':'cskisa@spacezone.kr'}
    d2 = {101:'smart', 102:'graphic'}
    d3 = {'one':[101, 102, 103]}     # value에 리스트도 가능

    # 암호화된 상태로 출력
    print("암호화된 상태:")
    print(d1)
    print("그 외 딕셔너리들:")
    print(d2)
    print(d3)

    # 비밀번호 복호화해서 출력
    print("\n복호화된 비밀번호:")
    decrypted_passwd = decrypt_password(d1['passwd'])
    print(f"ID: {d1['id']}, 비밀번호: {decrypted_passwd}, 이메일: {d1['email']}")

# ch07_dic_2.py
if selected_program == 7:
    # Step 01 - 딕셔너리에 새 요소 추가
    a = {101: 'smart'}
    a[201] = 'graphic'      # key=201, value='graphic' 추가
    print(a)

# ch07_dic_3.py
if selected_program == 8:
    # Step 01 -딕셔너리에 새 요소 추가
    a = {101: 'smart'}
    a[201] = 'graphic'      # key=201, value='graphic' 추가
    print(a)
    # Step 02 -문자열 key 와 value 추가
    a = {101: 'smart', 201: 'graphic'}
    a['id'] = 'cskisa'
    print(a)
    # Step 03 - value에 리스트도 추가가능 (pdf에서는 추가가 안되어있어서 제가 따로 추가했습니다.)
    a = {101: 'smart', 201: 'graphic', 'id': 'cskisa'}
    a['one'] = [101, 102, 103]
    print(a)

# ch07_dic_4.py
if selected_program == 9:
    # Step 01 -현재 딕셔너리 출력
    a = {101: 'smart', 201: 'graphic', 'id': 'cskisa', 'one': [101, 102, 103]}
    print(a)
    # Step 02 -'one' 요소 삭제
    del a['one']
    print(a)

# ch07_dic_5.py
if selected_program == 10:
    # Step 03 -정수 key를 가진 요소 삭제
    a = {101: 'smart', 201: 'graphic', 'id': 'cskisa'}
    del a[201]              # key가 정수일때도 동일
    print(a)

# ch07_dic_6.py
if selected_program == 11:
    # Step 01 -현재 딕셔너리 출력
    a = {101: 'smart', 'id': 'cskisa'}
    print(a)

# ch07_dic_7.py
if selected_program == 12:
    # Step 02 -문자열 key로 추출
    a = {101: 'smart', 'id': 'cskisa'}
    print(a['id'])           # key가 'id'인 요소의 값
    # Step 03 -정수 key로 추출
    print(a[101])            # key가 101인 요소의 값

# ch07_dic_8.py
if selected_program == 13:
    # 동일한 key를 가진 딕셔너리 선언
    a = {101: 'space', 101: 'zone'}
    print(a[101])

# ch07_dic_9.py
if selected_program == 14:
    # 중복key 선언 후 a 자체를 출력
    a = {101: 'space', 101: 'zone'}
    print(a)

# ch07_dic_10.py
# 리스트를 key로 사용 (오류발생)
# a = {[1, 2]: 'speed'}

# ch07_dic_11.py
if selected_program == 15:
    # 튜플을 key로 사용(정상동작)
    a = {(1, 2): 'speed'}
    print(a[(1, 2)])

# ch07_dic_12.py
if selected_program == 16:
    # Step 01 -keys() 함수로 key 리스트 반환
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(a.keys())
    # Step 02 -list()로 dict_keys 객체를 리스트로 변환
    print(list(a.keys()))

# ch07_dic_13.py
if selected_program == 17:
    # Step 01 -values() 함수로 value 리스트 반환
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(a.values())
    # Step 02 -list()로 dict_values를 리스트로 변환
    print(list(a.values()))

# ch07_dic_14~15.py
if selected_program == 18:
    # Step 01 -items() 함수 사용
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(a.items())
    # Step 02 -list()로 dict_items를 리스트로 변환
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(list(a.items()))

# ch07_dic_16~17.py
if selected_program == 19:
    # Step 01 -get() 함수사용
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(a.get('id'))
    # Step 02 -정상 추출
    print(a.get('pw'))
    # Step 03 -존재하지 않는 key
    print(a.get('name'))     # None 반환(오류X)
    #print(a['name'])         # KeyError 발생!

# ch07_dic_18.py
if selected_program == 20:
    # get(key, 기본값) -key가없으면기본값반환
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print(a.get('name', 'non-name'))

# ch07_dic_19~20.py
if selected_program == 21:
    # Step 01 -존재하지않는key 조사
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    print('name' in a)
    # Step 02 -존재하는key 조사
    print('pw' in a)

# ch07_dic_21.py
if selected_program == 22:
    # clear() 함수로 모든 요소 삭제
    a = {'id': 'cskisa', 'pw': 123456, 'email': 'cskisa@spacezone.kr'}
    a.clear()
    print(a)

# ch07_set_1~2.py
if selected_program == 23:
    # Step 01 -리스트로 집합 생성
    s1 = set([1, 'two', 3])
    print(s1)
    # Step 02 -다양한 데이터 타입의 요소를 가진 집합
    s2 = set(['one', 2, 'three'])
    print(s2)

# ch07_set_3.py
if selected_program == 24:
    # 문자열을 집합으로 변환 (중복 제거)
    s3 = set('speed')
    print(s3)

# ch07_set_4~5.py
if selected_program == 25:
    # Step 01 -& 연산자로 교집합
    s1 = set([1, 'two', 3])
    s2 = set(['one', 'two', 'three', 4, 5])
    print(s1 & s2)
    # Step 02 -intersection() 함수사용
    print(s2.intersection(s1))

# ch07_set_6.py
if selected_program == 26:
    # 합집합 (| 연산자)
    s1 = set([1, 'two', 3])
    s2 = set(['one', 'two', 'three', 4, 5])
    print(s1 | s2)

# ch07_set_7~9.py
if selected_program == 27:
    # Step 01 -차집합 (-연산자)
    s1 = set([1, 'two', 3])
    s2 = set(['one', 'two', 'three', 4, 5])
    print(s1 - s2)
    # Step 02 -반대방향 차집합
    print(s2 - s1)
    # Step 03 -difference() 함수사용
    print(s1.difference(s2))
    # Step 04 -difference() 함수(반대방향)
    print(s2.difference(s1))

# ch07_set_10.py
if selected_program == 28:
    # add() 함수로요소1개추가
    sd = set([101, 102, 103])
    sd.add(105)
    print(sd)

# ch07_set_11.py
if selected_program == 29:
    # update() 함수로 여러 요소 추가
    sd = set([201, 203, 205])
    sd.update([202, 204])
    print(sd)

# ch07_set_12.py
if selected_program == 30:
    # remove() 함수로 특정 요소 제거
    sd = set([501, 502, 503])
    sd.remove(502)
    print(sd)