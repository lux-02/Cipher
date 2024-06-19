'''
MAC-CBC 구현 단계
1. 블록 암호 키 공유: AES 키를 생성하고, 이를 공유 키로 사용합니다.
2. CBC 모드로 메시지 전체 암호화: 메시지를 블록 단위로 나누어 암호화합니다.
3. 최종 블록을 MAC 값으로 이용: 암호화 과정의 마지막 블록을 MAC 값으로 사용합니다.
'''

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def generate_key():
    # 256-bit AES 키 생성
    return os.urandom(32)

def cbc_mac_encrypt(key, data):
    # AES 블록 크기
    block_size = AES.block_size

    # 메시지 패딩
    padded_data = pad(data, block_size)
    
    # 초기화 벡터 (IV) 생성
    iv = bytes([0] * block_size)  # IV를 0으로 초기화
    
    # AES CBC 모드 암호화 객체 생성
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 메시지 암호화
    encrypted_data = cipher.encrypt(padded_data)
    
    # 최종 블록을 MAC 값으로 사용
    mac = encrypted_data[-block_size:]
    
    return mac

def verify_mac(key, data, mac):
    # AES 블록 크기
    block_size = AES.block_size

    # 메시지 패딩
    padded_data = pad(data, block_size)
    
    # 초기화 벡터 (IV) 생성
    iv = bytes([0] * block_size)  # IV를 0으로 초기화
    
    # AES CBC 모드 암호화 객체 생성
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 메시지 암호화
    encrypted_data = cipher.encrypt(padded_data)
    
    # 최종 블록을 MAC 값으로 사용
    calculated_mac = encrypted_data[-block_size:]
    
    return calculated_mac == mac

# 테스트
if __name__ == "__main__":
    key = generate_key()
    message = b"Hello, this is a test message."

    # MAC 생성
    mac = cbc_mac_encrypt(key, message)
    print(f'MAC: {mac.hex()}')

    # MAC 검증
    is_valid = verify_mac(key, message, mac)
    print(f'Is MAC valid? {is_valid}')
