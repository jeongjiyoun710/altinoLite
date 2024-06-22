def fn_findMaxNumber(a,b,c):
    if(a>=b and a>=c):
        return a
    else:
        if(b>=c):
            return b
        else:
            return c


if(__name__ == "__main__"):
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    num3 = int(input("세번째 숫자 : "))


    result = fn_findMaxNumber(num1, num2, num3)
    print("가장 큰 수 : ", result)