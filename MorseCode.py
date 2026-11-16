table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), 
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'), 
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), 
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), 
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), 
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), 
         ('Y', '-.--'), ('Z', '--..')]

def encode(message):
    encoded_message = '' # 인코딩된 메시지 저장
    for char in message:
        if char.upper() in dict(table):
            encoded_message += dict(table)[char.upper()] + ' ' 
        else:
            encoded_message += char + ' ' 
    return encoded_message.strip() # 마지막 공백 제거

def encode_slow(message): 
    idx = ord(message.upper()) - ord('A') # 문자의 아스키 코드 값을 이용하여 인덱스 계산
    if 0 <= idx < len(table): 
        return table[idx][1] 
    else:
        return None 

def decode(morse_code):
    morse_dict = {code: char for char, code in table} 
    decoded_message = ''
    words = morse_code.split('   ')  # 문자를 구분하기 위해 3개의 공백으로 단어를 나눔
    for word in words:
        letters = word.split()  # 각 단어를 공백으로 나누어 문자로 분리
        for letter in letters:
            if letter in morse_dict:
                decoded_message += morse_dict[letter]
            else:
                decoded_message += '?'  # 알 수 없는 문자는 '?'로 표시
        decoded_message += ' '  # 단어 사이에 공백 추가
    return decoded_message.strip()

def decode_slow(code): # 이진 트리를 이용한 디코딩
    for e in table: 
        if e[1] == code: 
            return e[0] 
    return None 

