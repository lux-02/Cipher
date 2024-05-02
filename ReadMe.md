# CIPHER

암호화: C=Ek(P)

복호화: P=Dk(C)

대칭 암호: Key 동일

비대칭 암호: 공개 Key로 암호화, 개인 Key로 복호화

키 공간 (Key Space): 해독 가능성, 확률 범위

시저 암호: 평행 이동으로 암호화(Shift) → 전사 공격(Brute Force) 가능

단일 치환 암호: 치환 테이블로 암호화 → 빈도 분석 공격 가능 (최빈도에 따른 패턴 분석)

애니그마: 날짜별 키가 기록된 코드북으로 암호화

- 통신키 암호화 → 설치 순서 및 각도
- 통신문 암호화 → 설치 각도

일회용 패드: 평문 XOR 랜덤 비트 (ASCII 부호화 XOR 랜덤 비트열)

⇒ 복호화해도 올바른 평문인지 판정하는게 불가능 → 그렇기 때문에 해독할 수 없다.

DES: 평문을 64bit 블록으로 나눔 → 각각의 블록을 DES로 암호화(Key 56bit)

1. L - 32bit / R - 32bit
2. R → F(k1) → L XOR R(Fk1)
3. L XOR R ⇒ 64bit
4. 3회 반복 ⇒ Festel Network 3Round

⇒ CPA 선택 평문 공격 가능 (단, 해독자가 임의의 평문을 암호화할 수 있다는 전제하에 가능)

Triple-DES

- DES-EDE2: 암호화(k1) → 복호화(k2) → 암호화(k1)

* 1, 3번째 키 동일

- DES-EDE3: 암호화(k1) → 복호화(k2) → 암호화(k3)

* Key가 다 다름

AES: Rijndael

---

Block 암호화: 집합 형태의 블록에 대해 각각 암호화하는 방식
평문을 블록화하고, 공간이 남으면 패딩 추가
(DES: 64bit / AES: 128, 192, 256bit)
Stream 암호화: 1, 8, 32bit씩 순차적으로 처리하는 방식

- IV = Initialize Vector (난수 블록)

DES Mode

- ECB (Electric Code Book)
  재전송 공격 가능 1. P1 → 암호화 → C1 2. P2 → 암호화 → C2 3. P3 → 암호화 → C3 4. P4 → 암호화 → C4
- CBC (Cipher Block Chaining) / 권장
  암호문 블록을 XOR하고 암호화 1. P1 [XOR] IV → 암호화 → C1 2. P2 [XOR] C1 → 암호화 → C2 3. P3 [XOR] C2 → 암호화 → C3 4. P4 [XOR] C3 → 암호화 → C4
- CFB (Cipher Feed Back)
  암호문 블록을 암호화한 후 XOR
  재전송 공격 가능 1. IV → 암호화 → C0 2. P1 [XOR] (C0 → 암호화) → C1 3. P2 [XOR] (C2 → 암호화) → C2 4. P3 [XOR] (C3 → 암호화) → C3 5. P4 [XOR] (C4 → 암호화) → C4
- OFB (Output Feed Back) \* 스트림 암호
  초기 암호화 블록을 계속 암호화하여 사용
  비트 반전 공격 가능 1. IV → 암호화 → X0 2. P1 [XOR] (X0 → 암호화 → X1) → C1 3. P2 [XOR] (X1 → 암호화 → X2) → C2 4. P3 [XOR] (X2 → 암호화 → X3) → C3 5. P4 [XOR] (X3 → 암호화 → X4) → C4
- CTR (Counter) \* 스트림 암호 / 권장
  카운터 값에 +1씩 증가시켜 암호화 수행
  비트 반전 공격 가능 1. P1 [XOR] (Counter+1 → 암호화 → X1) → C1 2. P2 [XOR] (Counter+2 → 암호화 → X2) → C2 3. P3 [XOR] (Counter+3 → 암호화 → X3) → C3 4. P4 [XOR] (Counter+4 → 암호화 → X4) → C4

키 전달 방식

- KDC: 키 배포 센터에서 일시적인 세션키를 공유하는 방식
  센터 과부하 및 센터 공격 - 중앙집중화의 단점
- Diffie-Hellman: 정보 교환 후 동일 키 생성 (공개키 방식)

공개 키 암호 방식:

- 암호화 키는 공개되어 있어서 누구나 암호화 가능, 복호화 키는 특정 개인만 가지고 있음

1. Key Pair = K(pub) / K(pri) 생성
2. K(pub) 전송 → C = E[K(pub), P] 암호화
3. P = D[K(pri), C] 복호화

시계 계산

- 덧셈: (A + B) MOD 12
- 뺄셈: (A + X) MOD 12 = 0 → X 계산
- 곱셈: (A \* B) MOD 12
- 나눗셈: (A \* X) MOD 12 = 1 → X 계산

MOD 12에서 역수를 갖는 수는 1, 12 이외의 공통 약수를 가지지 않는 수이다.

⇒ 1, 5, 7, 11

7^4 MOD 12 = 1

RSA

⇒ E = P^E MOD N → 공개키 E, N

⇒ P = C^D MOD N → 개인키 D, N

1. 2개의 소수 p, q 선택
2. N ⇒ p \* q
3. L ⇒ lcm(p-1, q-1)
   L은 키 쌍 생성에만 사용, p-1과 q-1의 최소공배수
4. E ⇒ gcd(E, L) = 1
   E와 L은 서로소 관계, 1<E<L
5. D ⇒ E \* D mod L = 1
   1<D<L

예시

1. p=17, q=19
2. N = 17 \* 19 = 323
3. L = lcm(16, 18) = 144
4. E = gcd(E, 144) = 1 → E = 5, 7, 11, 13, 17 …
   E = 5로 선택
5. D ⇒ 5 \* D mod 144 = 1 → D = 29

그러므로 공개키(E, N) = (5, 323) , 개인키(D, N) = (29, 323)

암호문을 평문으로 복호화하기 위해선 공개된 N을 기준으로 p, q 소수를 구해야 하므로,
고속으로 소인수분해 할 수 있는 방법이 있다면 RSA를 깰 수 있다.

중간자 공격

A가 B에게 공개키를 요청할 때,

C가 B의 공개키를 가지고, A에게 C의 공개키를 전달

A가 C의 공개키로 암호화한 평문을 B에게 전달

C가 중간에서 탈취 후 평문 확보, 다시 B의 공개키로 암호화하여 B에게 전달

공개키 방식은 같은 정도의 기밀성을 갖는 키 길이의 경우, 대칭 암호보다 몇 백배나 느림

긴 메시지를 암호화하기에 적합하지 않으며 중간자 공격에 약하기 때문에 대칭암호 방식과 병행하여 사용

하이브리드 암호 - PGP, SSL/TLS

C1 = E[K, P] → 대칭 암호화 메시지 → 복호화시 P = D(K, C1)

C2 = E[K(pub), K] 공개키 암호화 세션키 → 복호화시 개인키 K(pri) 필요 K = D[K(pri), C2]

C = C1 || C2 = E[K, P] || E[K(pub), K]

대칭 암호 및 공개키 암호 키길이는 양쪽 같은 정도의 강도가 되도록 밸런스 맞추기

장기간 운용시 대칭 암호보다 공개키 암호를 강하게 해야함
