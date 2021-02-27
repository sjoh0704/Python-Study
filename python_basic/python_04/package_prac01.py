# 모듈과 패키지
class Calculator:
    def plus(x, y):
        return x + y
    def minus(x, y):
        return x - y
    def multi(x, y):
        return x * y
    def divide(x, y):
        return x // y


#  단위 실행(독립적으로 파일 실행)
#  모듈 사용전 실험해보기 좋다. 
if __name__ == '__main__':
    x, y = 10, 20
    print(Calculator.plus(y, x))
    print(Calculator.minus(y, x))
    print(Calculator.multi(y, x))
    print(Calculator.divide(y, x))
    
    
    
    