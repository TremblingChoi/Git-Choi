def display_multiplication_table1():
    for n in range(1,10):
        for i in range(2, 6):
            print(f'{i} x {n} = {n*i:2d}',end='\t')
        print()

def display_multiplication_table2():
    for n in range(1,10):
        for i in range(6, 10):
            print(f'{i} x {n} = {n*i:2d}',end='\t')
        print()

display_multiplication_table1()
print()
display_multiplication_table2()
