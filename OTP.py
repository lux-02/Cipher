'''
HOTP (HMAC-based One-Time Password)
생성 방식: HMAC-SHA-1 해시 함수를 사용하여 카운터 값과 비밀 키를 조합하여 OTP를 생성합니다.

HOTP 생성 과정
1. 비밀 키 K와 카운터 값 C 준비
2. HMAC-SHA-1 계산: HMAC-SHA-1 해시 함수를 사용하여 K와 C를 조합하여 해시 값을 생성합니다.
3. OTP 추출: 해시 값의 일부를 사용하여 최종 OTP를 생성합니다.


TOTP (Time-based One-Time Password):
생성 방식: 현재 시간과 비밀 키를 조합하여 OTP를 생성합니다. 일반적으로 30초나 60초 간격으로 OTP가 갱신됩니다.

TOTP 생성 과정
1. 비밀 키 K와 시간 값 T 준비:
T는 일반적으로 현재 시간을 일정 시간 간격(예: 30초)으로 나눈 값을 사용합니다.
2. HMAC-SHA-1 계산: HMAC-SHA-1 해시 함수를 사용하여 K와 T를 조합하여 해시 값을 생성합니다.
3. OTP 추출: 해시 값의 일부를 사용하여 최종 OTP를 생성합니다.

'''

# HOTP
import hmac
import hashlib
import struct

def hotp(key, counter, digits=6):
    counter_bytes = struct.pack('>Q', counter)
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    code = (struct.unpack('>I', hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF) % (10 ** digits)
    return code

key = b'secret_key'
counter = 1
print(f'HOTP: {hotp(key, counter)}')


# TOTP
import time

def totp(key, time_step=30, digits=6):
    current_time = int(time.time() // time_step)
    return hotp(key, current_time, digits)

key = b'secret_key'
print(f'TOTP: {totp(key)}')
