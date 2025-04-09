def read_single_digit(d):
    if d == 0:
        return "영"
    elif d == 1:
        return "일"
    elif d == 2:
        return "이"
    elif d == 3:
        return "삼"
    elif d == 4:
        return "사"
    elif d == 5:
        return "오"
    elif d == 6:
        return "육"
    elif d == 7:
        return "칠"
    elif d == 8:
        return "팔"
    elif d == 9:
        return "구"
        
def read_number(n):
    num_str = str(n)
    return (
        read_single_digit(int(num_str[0])) + " " +
        read_single_digit(int(num_str[1])) + " " +
        read_single_digit(int(num_str[2]))
    )

a=int(input('세 자리 정수 입력: '))
print (read_number(a))
