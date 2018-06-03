def main():
    """打印前 20 项斐波那契数列：a_1=1, a_2 = 1,a_n = a_n-1 + a_n-2"""
    fib = [101]
    fib[0] = 1
    fib[1] = 1
    for i in fib:

        fib[i] = fib[i - 1] + fib[i - 2]


if __name__ == "__main__":
    main()
