def rep_char(c, n):
    print(c * n)

def draw_line_string(s):
    msg1 = 'Hello '+s
    msg2 = ('Welcome to Seoul')
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)

name=input('input his/her name: ')
draw_line_string(name)
