def main():
    """输入n个数求平均数"""
    n = int(input("请输入数字个数:"))  # 需要循环的次数
    s_num = 0
    cnt = 0  # 计数器

    while n > cnt:

        num = float(input("请输入数字:")) # 需要求的数
        s_num += num
        cnt += 1

    print("平均数为:%.2f" % (s_num / n))


if __name__ == "__main__":
    main()
