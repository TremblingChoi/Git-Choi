shopping_bag={}
while True:
    item=input('상품명? ')
    if item == "":
        break
    n=int(input('수량은? '))
    shopping_bag[item] = n
    print(f"장바구니에 {item}{n}개가 담겼습니다.\n")

print("\n>>> 장바구니 보기:",shopping_bag)
print("\n[검색]")
s=input("장바구니에서 확인하고자 하는 상품은? ")
if s in shopping_bag:
    print(f"{s}은(는) {n}개 담겨 있습니다.")
else:
    print(f"{s}(이)라는 이름의 상품은 없습니다.")
