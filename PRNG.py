'''
PRNG(Pseudorandom Number Generator)
시드 확장 및 난수 생성
'''
import hashlib

class SimplePRNG:
    def __init__(self, seed):
        self.seed = seed
        self.state = hashlib.sha256(seed.encode()).digest()

    def next(self):
        self.state = hashlib.sha256(self.state).digest()
        return int.from_bytes(self.state[:4], 'big')  # 첫 4 바이트를 정수로 변환하여 난수 생성

# 시드 설정
seed = "my_secure_seed"
prng = SimplePRNG(seed)

# 난수 생성
for _ in range(5):
    print(prng.next())
