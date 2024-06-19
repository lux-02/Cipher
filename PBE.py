'''
PBE (Password-Based Encryption)
PBKDF2 (Password-Based Key Derivation Function 2)
1. 비밀번호와 솔트 값을 입력받음
2. 지정된 횟수만큼 해시 함수를 반복적으로 적용하여 키를 생성
3. 생성된 키는 데이터 암호화에 사용
'''

import hashlib
import os

# 사용자 비밀번호 입력
password = b'password123'
# 임의의 소금 생성
salt = os.urandom(16)

# PBKDF2를 사용하여 키 생성 (SHA-256 해시 함수 사용)
key = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)

print(f'Salt: {salt.hex()}')
print(f'Key: {key.hex()}')
