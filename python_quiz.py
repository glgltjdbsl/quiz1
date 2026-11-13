# ============================================================
#  Part A. Python 문제 (50점)
#  - 문제 설명은 문제지.pdf 에 있습니다.
#  - 함수 이름, 클래스 이름, 매개변수는 바꾸지 마세요. (자동 채점됩니다)
#  - 결과는 print 가 아니라 반드시 return 으로 돌려주세요.
#  - pass 를 지우고 코드를 작성하세요.
#  - 다 풀고 나면  python3 python_quiz.py  로 실행해서
#    에러 없이 예시 결과가 나오는지 꼭 확인하세요.
# ============================================================


# ------------------------------------------------------------
# 문제 1. 배달비 계산 (8점)
# ------------------------------------------------------------
def delivery_fee(total, distance):
    return (total + distance)

def main():
    total = int(input("주문 금액(원)"))
    distance = float(input("배달 거리(km)"))
    if total >= 30000:
        fee = 0
    elif distance < 2:
        fee = 2000
    elif 2<= distance <5:
        fee = 3000
    elif distance >= 5:
        fee = 5000
    print("최종 금액 : {0}원" .format(total+fee))

if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# 문제 2. 운동장 이벤트 당첨자 찾기 (12점)
# ------------------------------------------------------------
def find_winners(numbers):
    winners = []

    for i in range(len(numbers)):
        num = numbers[i]

        if 10 <= num <= 17:
            winners.append(i + 1)

    return winners


def main():
    numbers = [10, 20, 17, 9]
    print(find_winners(numbers))


if __name__ == "__main__":
    main()


# ------------------------------------------------------------
# 문제 3. 주문 금액 계산 (12점)
# ------------------------------------------------------------
# 문제 3. 주문 금액 계산 (12점)
# ------------------------------------------------------------
def order_total(menu, orders):
    ls = list(menu.keys())
    count=0
    cc=0
    for i in range(len(ls)):
        if ls in menu.keys:
            count=count+1
            price = menu.values()
        else:
            cc=cc+1
        print("({0}, {1})" .format(price, cc))
price=0

menu = {"비빔우동": 7000, "튀김우동": 8000, "유부초밥": 4000}

#print(menu["비빔우동"])

#print(#입력 in menu)        #menu에 있는지 확인
    
#print(menu.values())        #key 값 금액 반환

#c=menu.count("비빔우동")        #몇 번 횟수
#c=menu.count("튀김우동")
#c=menu.count("유부초밥")

order_total(menu, ["비빔우동", "유부초밥", "비빔우동", "돈까스"])


# ------------------------------------------------------------
# 문제 4. 비빔우동 키오스크 2.0 (18점)
# ------------------------------------------------------------
# (1) 여기에 SoldOutError 클래스를 직접 만드세요.
class SoldOutError(Exception):
    def __init__(self, errmsg):
        self.errmsg=errmsg
    def __str__(self):
        return self.errmsg

class UdonKiosk:
    PRICE = 7000  # 비빔우동 한 그릇 가격

    def __init__(self, stock):
        self.stock = stock

    def order(self, text):
        self.text = text

    def total_sales(self):
        pass

try:
    udong=UdonKiosk()
    while True:
        order = int(input("우동 몇 그릇 주문하실까요? "))
        if order < 1:
            raise ValueError
        elif stock < order:
            raise ValueError
        elif stock == 0:
            raise SoldOutError("매진")

except ValueError:
    print("정수만 입력")
    
except SoldOutError as error:
    print(error)

UdonKiosk(3)


# ============================================================
#  아래는 확인용 코드입니다. 수정하지 않아도 됩니다.
#  python3 python_quiz.py 로 실행하면 문제지의 예시와 비교할 수 있습니다.
# ============================================================
def main():
    menu = {"비빔우동": 7000, "튀김우동": 8000, "유부초밥": 4000}
    try:
        print("문제 1 :", delivery_fee(12000, 3))            # 3000
        print("문제 2 :", find_winners([10, 20, 17, 9]))     # [1, 3]
        print("문제 3 :", order_total(menu, ["비빔우동", "유부초밥", "비빔우동", "돈까스"]))  # (18000, 1)
        kiosk = UdonKiosk(3)
        print("문제 4 :", kiosk.order("2"))                  # 14000
        print("문제 4 :", kiosk.stock, kiosk.sold)           # 1 2
        print("문제 4 :", kiosk.total_sales())               # 14000
    except Exception as e:
        print("에러 발생 :", type(e).__name__, e)


if __name__ == "__main__":
    main()
