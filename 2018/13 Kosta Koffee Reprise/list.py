with open("list.txt", 'w') as f:
    for i in range(1159, 1000000):
        num = str(i)
        if num.count("1") == 2 and "5" in num and "9" in num:
            print(num)
            f.write("{0:0=6d}".format(i) + "\n")
