def read_single_digit(d):
    digit_to_korean = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return digit_to_korean[d]

def read_number(n):
    num_str = str(n)
    return (
        read_single_digit(int(num_str[0])) + " " +
        read_single_digit(int(num_str[1])) + " " +
        read_single_digit(int(num_str[2]))
    )

a=int(input('세 자리 정수 입력: '))
print (read_number(a))
