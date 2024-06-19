'''
디지털 서명 

1. RSA 키 생성:
generate_rsa_keypair 함수는 RSA 키 쌍을 생성합니다. private_key는 개인키이고, public_key는 공개키입니다.

2. 메시지 서명 생성:
sign_message 함수는 주어진 메시지를 개인키로 서명합니다.
메시지를 해시(SHA-256)로 변환하고, 개인키로 서명합니다.

3. 서명 검증:
verify_signature 함수는 주어진 서명이 공개키와 메시지에 대해 유효한지 검증합니다.
메시지를 해시(SHA-256)로 변환하고, 공개키로 서명을 검증합니다.

'''

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# RSA 키 생성
def generate_rsa_keypair(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

# 메시지 서명 생성
def sign_message(private_key, message):
    # 메시지 해시 생성
    h = SHA256.new(message.encode('utf-8'))
    # 개인키로 서명 생성
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

# 서명 검증
def verify_signature(public_key, message, signature):
    # 메시지 해시 생성
    h = SHA256.new(message.encode('utf-8'))
    try:
        # 공개키로 서명 검증
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# 테스트
if __name__ == "__main__":
    # 키 쌍 생성
    private_key, public_key = generate_rsa_keypair()

    # 메시지
    message = "Hello, RSA Digital Signature!"

    # 서명 생성
    signature = sign_message(private_key, message)
    print(f'Signature: {signature.hex()}')

    # 서명 검증
    is_valid = verify_signature(public_key, message, signature)
    print(f'Is the signature valid? {is_valid}')

    # 서명 위조 테스트
    forged_message = "This is a forged message."
    is_valid = verify_signature(public_key, forged_message, signature)
    print(f'Is the forged signature valid? {is_valid}')
