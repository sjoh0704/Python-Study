# 상속, 다중상속

class Car:
    """ Parent class"""

    def __init__(self, tp, color) -> None:
        self.type =tp
        self.color = color
    def show(self):
        return "car class' show method"

class BmwCar(Car):
    """ sub class"""
    def __init__(self, car_name, tp, color):
        self.car_name = car_name
        super().__init__(tp, color)  # 부모 클래스를 상속받았으므로 이용하자

    def show_model(self):
        return "your car name :{}".format(self.car_name)


    # 메소드 오버라이딩
    
    def show(self):
        print("show: %s %s %s" %(self.car_name, self.type, self.color ))


bmw1 = BmwCar("abc", "xxx", "red")

bmw2 = BmwCar("aaa", "yy", "blue")
print(bmw1.show_model())
print(bmw2.show_model())
bmw1.show()




