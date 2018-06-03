def f(n):
    """阶乘的计算"""
    result = 1
    for x in range(n + 1):
        if x == 0:
            continue
        result *= x
    return result


def X(x, n):
    """对幂级数每一项的计算 e^x = 1 + x + x^2/2! + x^3/3! +...+ x^n/n! """
    return x ** n / f(n)


def main():
    """对于幂级数：e^x = 1 + x + x^2/2! + x^3/3!+ … 分别求出前 2、5、10 项的求和结果"""
    x = float(input("请输入x的值:"))
    x_sum = 0
    for a in range(11):
        if a == 2 or a == 5 or a == 10:
            for y in range(a):

                x_sum += X(x, y)

            print("The first {} item sum is {}".format(a, x_sum))
            return x_sum

if __name__ == "__main__":

    main()
