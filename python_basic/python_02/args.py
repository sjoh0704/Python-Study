# 매개변수가 몇개 필요한지 모를때 튜플형태로 준다.

def args_func(*args):

    for i, v in enumerate(args):
        print(i, v)

args_func("kim")
args_func("kim", "oh", "choi")


# 딕셔너리를 인자로 받을때 
def kargs_func(**kwargs):

    for k, v in kwargs.items():
        print(k, v)

kargs_func(name1="kim", name2="oh")


# 혼합

def example(args1, args2, *args3, **args4):
    print(args1)
    print(args2)
    for i, v in enumerate(args3):
        print(i, v)
    for k, v in args4.items():
        print(k, v)

example("a","b","c","d","e",next="f", next2="g")


# 중첩함수 클로저

def nested_func(num):
    def func_in_func(num):   # 함수 내부에서 함수 선언 
        print(num)
    print("in func")
    func_in_func(num+10000)
nested_func(10000)


def func_mul(x:int) -> list:
    y = x * 2
    y2 = x * 3
    return [y, y2]
print(func_mul(3))