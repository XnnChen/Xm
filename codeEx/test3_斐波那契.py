def main():
    """打印前 20 项斐波那契数列：a_1=1, a_2 = 1,a_n = a_n-1 + a_n-2"""
    a1, a2 = 1, 1
    i = 0
    while i < 20:
        i += 1
        if i > 1:
            a1, a2 = a2, a1 + a2
        print(a1)


if __name__ == "__main__":
    main()
