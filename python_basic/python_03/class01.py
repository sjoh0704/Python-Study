class UserInfo:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def not_self_method1(self):  
        print("I don't have self")


    # self가 없으면 클래스를 통해서 직접 호출할 수 있다. 
    def not_self_method2():  # 클래스 메소드  
        print("I don't have self")

user1 = UserInfo("승", 26)
# print(user1.__dict__)

user1.not_self_method1()
UserInfo.not_self_method2()


