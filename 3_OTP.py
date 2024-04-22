import random
import string

def generate_key(length):
    """ 무작위 키 생성 """
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(message, key):
    """ 메시지 암호화 """
    message = message.upper()
    key = key.upper()
    encrypted = ''
    for m, k in zip(message, key):
        # A=0, B=1, ..., Z=25으로 계산
        encrypted_char = (ord(m) - ord('A') + ord(k) - ord('A')) % 26 + ord('A')
        encrypted += chr(encrypted_char)
    return encrypted

def decrypt(ciphertext, key):
    """ 암호문 복호화 """
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted = ''
    for c, k in zip(ciphertext, key):
        decrypted_char = (ord(c) - ord(k)) % 26 + ord('A')
        decrypted += chr(decrypted_char)
    return decrypted

# 사용 예시
message = "HELLO WORLD"
key = generate_key(len(message))
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Message:", message)
print("Key:", key) #Key: MYJUREUFSWB
print("Encrypted:", encrypted_message) #Encrypted: TCUFFXQTJHE
print("Decrypted:", decrypted_message) #Decrypted: HELLOTWORLD
