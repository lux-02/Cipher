'''
PGP(Pretty Good Privacy)
1. 키 쌍 생성: generate_rsa_keypair 함수는 RSA 키 쌍을 생성합니다.
2. PGP 암호화 과정:
- 대칭 키 생성: session_key = get_random_bytes(16)는 AES를 위한 대칭 키를 생성합니다.
- 메시지 암호화: AES를 사용하여 메시지를 암호화합니다.
- 대칭 키 암호화: RSA를 사용하여 대칭 키를 암호화합니다.
3. PGP 복호화 과정:
- 대칭 키 복호화: RSA를 사용하여 대칭 키를 복호화합니다.
- 메시지 복호화: 복원된 대칭 키를 사용하여 AES로 암호문을 복호화합니다.
'''


from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# RSA 키 쌍 생성
def generate_rsa_keypair(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

# PGP 암호화 과정
def pgp_encrypt(public_key, message):
    # 대칭 키 생성
    session_key = get_random_bytes(16)
    
    # 메시지 암호화 (AES 사용)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode('utf-8'))
    
    # 대칭 키 암호화 (RSA 사용)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    
    return enc_session_key, cipher_aes.nonce, tag, ciphertext

# PGP 복호화 과정
def pgp_decrypt(private_key, enc_session_key, nonce, tag, ciphertext):
    # 대칭 키 복호화 (RSA 사용)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    
    # 메시지 복호화 (AES 사용)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    return message.decode('utf-8')

# 테스트
if __name__ == "__main__":
    private_key, public_key = generate_rsa_keypair()
    message = "Hello, this is a PGP-like encrypted message!"

    # 암호화
    enc_session_key, nonce, tag, ciphertext = pgp_encrypt(public_key, message)
    print(f'Encrypted Session Key: {enc_session_key.hex()}')
    print(f'Nonce: {nonce.hex()}')
    print(f'Tag: {tag.hex()}')
    print(f'Ciphertext: {ciphertext.hex()}')

    # 복호화
    decrypted_message = pgp_decrypt(private_key, enc_session_key, nonce, tag, ciphertext)
    print(f'Decrypted Message: {decrypted_message}')
