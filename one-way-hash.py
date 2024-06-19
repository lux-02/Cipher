'''
One-way hash Function
입력되는 숫자를 23으로 나누어 몫을 소수로 표현 → 소숫점 이하 7자리 ~ 10자리 4개
'''

def extract_hash_value(number):
    # 23으로 나누기
    division_result = number / 23
    
    # 소수점 이하 부분을 문자열로 변환
    decimal_part_str = str(division_result).split('.')[1]
    
    # 소수점 이하 7자리에서 10자리 추출
    if len(decimal_part_str) >= 10:
        hash_value = decimal_part_str[6:10]
    else:
        # 소수점 이하 자릿수가 10자리보다 짧으면 0으로 패딩
        decimal_part_str = decimal_part_str.ljust(10, '0')
        hash_value = decimal_part_str[6:10]
    
    return hash_value

# 테스트
input_number = 345689
hash_result = extract_hash_value(input_number)
print(f'Input Number: {input_number}')
print(f'Hash Value: {hash_result}')
