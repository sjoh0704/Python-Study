def mul_10(num: int) -> int:
    return num * 10

var_func = mul_10
print(var_func)  # 함수가 실행되기도 전에 객체가 생성되고 메모리에 할당 

print(var_func(10))


# 람다이용하기 

lam_mul_10 = lambda x: x*10
print(lam_mul_10(10))
