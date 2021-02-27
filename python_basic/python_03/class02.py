class WareHouse:

    # 클래스 변수도 마찬가지로 self가 없음
    # 클래스 변수는 객체보다 먼저 생성 
    stock_num = 0 

    def __init__(self, name) -> None:
        self.name = name
        WareHouse.stock_num += 1

    # 인스턴스가 사라질때 호출되는 메소드 

    def __del__(self):
        WareHouse.stock_num -= 1

    def get_stock_number():
        print("stock number: " +str(WareHouse.stock_num))

WareHouse.get_stock_number()

stock1 = WareHouse("kim")
stock2 = WareHouse("oh")

WareHouse.get_stock_number()

del stock1
WareHouse.get_stock_number()