from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import binascii

def pad(text):
    """PKCS#5 패딩 추가."""
    n = 8 - len(text) % 8
    return text + (chr(n) * n).encode()

def encrypt_ecb(plaintext, key):
    """DES ECB 모드로 텍스트 암호화."""
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    encrypted_text = des.encrypt(padded_text)
    return encrypted_text

def format_blocks(data, block_size=8):
    """데이터를 블록으로 나누고 16진수 형태로 포맷."""
    return [binascii.hexlify(data[i:i+block_size]).decode() for i in range(0, len(data), block_size)]

# 8바이트 (64비트) 키 생성
key = get_random_bytes(8)

# 암호화할 메시지
plaintext = b"Hello, Wolrd!"

# 암호화 실행
encrypted = encrypt_ecb(plaintext, key)

# 평문 및 암호문 블록 형태로 출력
plaintext_blocks = format_blocks(pad(plaintext))
encrypted_blocks = format_blocks(encrypted)

print("Plaintext Blocks:")
for block in plaintext_blocks:
    print(block)

print("\nEncrypted Blocks:")
for block in encrypted_blocks:
    print(block)
