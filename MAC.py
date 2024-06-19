'''
MAC(Message Authentication Code)
HMAC(Hash-based Message Authentication Code)
1. 비밀 키 패딩: 비밀 키가 해시 블록 크기보다 짧으면 오른쪽에 0으로 패딩하고, 길면 해시 함수를 적용하여 블록 크기로 줄입니다.
2. 내부 키와 외부 키 생성: 내부 키와 외부 키는 각각 비밀 키에 특정 값을 XOR한 결과입니다.
3. 해시 계산:
   - 내부 해시: 내부 키와 메시지를 결합하여 해시 함수를 적용합니다.
   - 외부 해시: 외부 키와 내부 해시 결과를 결합하여 다시 해시 함수를 적용합니다.
4. 최종 MAC 생성: 최종 해시 결과가 메시지 인증 코드 (MAC)가 됩니다.
'''
import hmac
import hashlib

# 비밀 키와 메시지
secret_key = b'secret_key'
message = b'This is a message.'

# HMAC 생성 (SHA-256 해시 함수 사용)
hmac_obj = hmac.new(secret_key, message, hashlib.sha256)
mac = hmac_obj.hexdigest()

print(f'Message: {message.decode()}')
print(f'MAC: {mac}')
