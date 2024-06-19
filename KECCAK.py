'''
SHA-3 / KECCAK 알고리즘 구현

keccak_f(state): KECCAK의 변환 함수입니다. 

24라운드에 걸쳐 θ, ρ, π, χ, ι 변환 단계를 수행합니다.

ROT(x, n): 64비트 단위의 비트 회전 함수입니다.

keccak_pad(message, rate): 입력 메시지를 패딩하는 함수입니다. KECCAK의 패딩 규칙에 따라 메시지를 패딩합니다.

keccak(message, rate, capacity): KECCAK 해시 함수입니다. 입력 메시지를 패딩하고, 각 블록을 흡수한 후, 변환 함수를 통해 해시 값을 짜냅니다.

테스트 코드: "Hello, KECCAK!"라는 메시지를 해시하여 KECCAK-256 해시 값을 출력합니다.
'''
import numpy as np

# KECCAK의 변환 함수 예시
def keccak_f(state):
    # 라운드 상수
    RC = [
        0x0000000000000001, 0x0000000000008082, 0x800000000000808a, 0x8000000080008000,
        0x000000000000808b, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009,
        0x000000000000008a, 0x0000000000000088, 0x0000000080008009, 0x000000008000000a,
        0x000000008000808b, 0x800000000000008b, 0x8000000000008089, 0x8000000000008003,
        0x8000000000008002, 0x8000000000000080, 0x000000000000800a, 0x800000008000000a,
        0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008
    ]

    def ROT(x, n):
        return ((x << n) & 0xFFFFFFFFFFFFFFFF) | (x >> (64 - n))

    for round in range(24):
        # Theta
        C = [int(state[x, 0] ^ state[x, 1] ^ state[x, 2] ^ state[x, 3] ^ state[x, 4]) for x in range(5)]
        D = [C[x-1] ^ ROT(C[(x+1) % 5], 1) for x in range(5)]
        for x in range(5):
            for y in range(5):
                state[x, y] = int(state[x, y]) ^ D[x]

        # Rho and Pi
        B = np.zeros((5, 5), dtype=np.uint64)
        for x in range(5):
            for y in range(5):
                B[y, (2*x + 3*y) % 5] = ROT(int(state[x, y]), ((x+1)*(y+1)) % 64)

        # Chi
        for x in range(5):
            for y in range(5):
                state[x, y] = int(B[x, y]) ^ ((~int(B[(x+1) % 5, y])) & int(B[(x+2) % 5, y]))

        # Iota
        state[0, 0] = int(state[0, 0]) ^ RC[round]

    return state

# 패딩 함수
def keccak_pad(message, rate):
    padded_message = message + b'\x01'
    while len(padded_message) % rate != 0:
        padded_message += b'\x00'
    padded_message = padded_message[:-1] + b'\x80'
    return padded_message

# KECCAK 해시 함수
def keccak(message, rate=1088, capacity=512):
    state = np.zeros((5, 5), dtype=np.uint64)
    rate_bytes = rate // 8

    # 메시지 패딩
    padded_message = keccak_pad(message, rate_bytes)

    # 메시지 흡수
    for i in range(0, len(padded_message), rate_bytes):
        block = padded_message[i:i+rate_bytes]
        block_bits = np.frombuffer(block, dtype=np.uint64)
        for j in range(len(block_bits)):
            x, y = j % 5, j // 5
            state[x, y] ^= block_bits[j]
        state = keccak_f(state)

    # 해시 값 짜내기
    output = b''
    while len(output) < capacity // 8:
        for y in range(5):
            for x in range(5):
                output += state[x, y].tobytes()
                if len(output) >= capacity // 8:
                    break
            if len(output) >= capacity // 8:
                break
        state = keccak_f(state)

    return output[:capacity // 8]

# 테스트
if __name__ == "__main__":
    message = b"Hello, KECCAK!"
    hash_value = keccak(message)
    print(f'Input Message: {message.decode()}')
    print(f'KECCAK-256 Hash: {hash_value.hex()}')
