def buy(shopping_bag):
    print("[구입]")
    item = input("상품명? ")
    if item == "":
        return False
        n = int(input("수량은? "))
        shopping_bag[item] = n
        print(f"장바구니에 {item} {n}개가 담겼습니다.\n")
        return True

def show(shopping_bag):
    print("\n>>> 장바구니 보기:", shopping_bag)

def find(shopping_bag):
    print("\n[검색]")
    s = input("장바구니에서 확인하고자 하는 상품은? ")
    if s in shopping_bag:
        print(f"{s}(은)는 {shopping_bag[s]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {s}(은)는 없습니다.")

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
