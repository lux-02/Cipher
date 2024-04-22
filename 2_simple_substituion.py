from prettytable import PrettyTable
import random

def generate_substitution_key():
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffled_letters = random.sample(letters, len(letters))
    return dict(zip(letters, shuffled_letters))

def print_key_table(key):
    table = PrettyTable()
    table.field_names = ["Original", "Substitution"]
    for k, v in key.items():
        table.add_row([k, v])
    print(table)

def encrypt_substitution(plaintext, key):
    encrypted = ""
    for char in plaintext.upper():
        if char in key:
            encrypted += key[char]
        else:
            encrypted += char 
    return encrypted

def decrypt_substitution(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted = ""
    for char in ciphertext:
        if char in reverse_key:
            decrypted += reverse_key[char]
        else:
            decrypted += char 
    return decrypted

key = generate_substitution_key()
print_key_table(key)

plaintext = "HELLO WORLD"
encrypted = encrypt_substitution(plaintext, key) #Encrypted: QXRRL MLZRC
print("Encrypted:", encrypted)

decrypted = decrypt_substitution(encrypted, key) #Decrypted: HELLO WORLD
print("Decrypted:", decrypted)

''' 
*** 매번 바뀌는 랜덤 테이블 ***
+----------+--------------+
| Original | Substitution |
+----------+--------------+
|    A     |      J       |
|    B     |      Y       |
|    C     |      H       |
|    D     |      C       |
|    E     |      X       |
|    F     |      O       |
|    G     |      T       |
|    H     |      Q       |
|    I     |      E       |
|    J     |      K       |
|    K     |      B       |
|    L     |      R       |
|    M     |      W       |
|    N     |      P       |
|    O     |      L       |
|    P     |      U       |
|    Q     |      N       |
|    R     |      Z       |
|    S     |      A       |
|    T     |      S       |
|    U     |      F       |
|    V     |      G       |
|    W     |      M       |
|    X     |      D       |
|    Y     |      V       |
|    Z     |      I       |
+----------+--------------+
'''