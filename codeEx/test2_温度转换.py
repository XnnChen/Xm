def main():
    """使用公式，将 0 到 200 度的华氏温度转换为摄氏温度：C = (F – 32)/1.8"""

    for f in range(201):
        print("F = %d: C = %.2f" % (f, (float(f - 32) / 1.8)))


if __name__ == "__main__":
    main()
