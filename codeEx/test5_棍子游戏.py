import random


def main():
    """棍子游戏"""
    stick = 21
    print("有21根棍子，一次能拿1 - 4根")
    print("谁拿到在最后一根就输了")

    while True:
        print("棍子数：", stick)
        stick_taken = int(input("拿棍子(1-4):"))
        if stick == 1:
            print("你拿到最后一根棍子，你输啦...")
            break
        elif stick <= 0:
            print("你赢啦...")
            break
        if stick_taken >= 5 or stick_taken <= 0:
            print("只能拿1-4根棍子")
            continue

        comput_taken = random.randint(1, 4)
        print("电脑拿：", comput_taken, "\n")


        stick -= stick_taken + comput_taken


if __name__ == "__main__":
    main()
