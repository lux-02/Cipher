'''
MAC(Message Authentication Code)
HMAC(Hash-based Message Authentication Code)

1. 키 길이 조정:
block_size = hashlib.sha256().block_size는 SHA-256 해시 함수의 블록 크기를 가져옵니다.
키가 블록 크기보다 길면 해시하여 줄이고, 블록 크기보다 짧으면 0으로 패딩합니다.

2. ipad와 opad 생성:
ipad는 키의 각 바이트를 0x36과 XOR하여 생성합니다.
opad는 키의 각 바이트를 0x5C와 XOR하여 생성합니다.

3. 첫 번째 해시 계산:
ipad와 메시지를 결합하여 해시 함수에 입력하고 첫 번째 해시 값을 계산합니다.

4. 두 번째 해시 계산:
opad와 첫 번째 해시 값을 결합하여 해시 함수에 입력하고 최종 HMAC 값을 계산합니다.
'''
import hashlib

def hmac_sha256(key, message):
    block_size = hashlib.sha256().block_size
    
    # 키 길이 조정
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')
    
    # ipad와 opad 생성
    ipad = bytes((x ^ 0x36) for x in key)
    opad = bytes((x ^ 0x5C) for x in key)
    
    # 첫 번째 해시 계산
    inner_hash = hashlib.sha256(ipad + message).digest()
    
    # 두 번째 해시 계산
    hmac = hashlib.sha256(opad + inner_hash).digest()
    
    return hmac

# 테스트
key = b'secret_key'
message = b'Hello, HMAC!'
hmac_result = hmac_sha256(key, message)
print(f'HMAC: {hmac_result.hex()}')
