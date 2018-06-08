def main():
    """将待拷贝文件“a.txt”第三行第二个单词，拷贝至目标文件“b.txt”"""

    # 1. 打开文件
    file_read = open("a.txt")
    file_write = open("b.txt", "w")

    # 2. 读取并写入文件
    text = file_read.readlines()
    line = text[2].split(" ")
    print(line[1])

    file_write.write(line[1])

    # 3. 关闭文件
    file_read.close()
    file_write.close()


if __name__ == "__main__":
    main()
