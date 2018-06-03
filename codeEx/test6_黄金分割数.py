def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n -2)


def main():
    """使用斐波那契数列，求出精确到 0.00001 的黄金分割数"""
    a = fib(19)
    b = fib(18)

    ans = b / a
    
    print("%.5f" % ans)
    # print(a)


if __name__ == "__main__":
    main()
