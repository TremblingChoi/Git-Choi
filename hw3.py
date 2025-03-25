def get_fixed_price(discount_rate, discounted_price):
    regular_price=discounted_price/(1-discount_rate/100)
    return regular_price

discount_rate=float(input('할인율은? '))
a_discounted_price=float(input('A 상품의 할인된 가격은? '))
b_discounted_price=float(input('B 상품의 할인된 가격은? '))

a_regular_price=get_fixed_price(discount_rate, a_discounted_price)
b_regular_price=get_fixed_price(discount_rate, b_discounted_price)

print('A 상품의 정가는 ',a_regular_price)
print('B 상품의 정가는 ',b_regular_price)
