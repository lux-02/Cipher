def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # 알파벳인 경우만 처리
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # 알파벳이 아닌 경우 변화 없이 추가
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # 복호화는 암호화의 역으로 수행

# 사용 예시
encrypted = caesar_encrypt("Hello, World!", 3)
print("Encrypted:", encrypted) #Encrypted: Khoor, Zruog!
decrypted = caesar_decrypt(encrypted, 3)
print("Decrypted:", decrypted) #Decrypted: Hello, World!
