import math


def main():
    print("这是一个软件老化可信度量模型。")

    # 输入数据
    input_data = [
        "5",
        "MEM 0.539",
        "STO 0.125",
        "LOG 0.238",
        "NUM 0.049",
        "ARU ",
        "0.0506 0.1845 0.0238 0.0238 0.0774 0.0774 0.0774 0.0238 0.0238 0.0506 0.0506 0.0238 0.0238 0.1042 0.1845",
        "0.25 0.25 0.25 0.25",
        "0.234 0.1064 0.1064 0.234 0.1064 0.1064 0.1064",
        "0.2 0.8",
        "0.1 0.9",
        "2",
        "0 10",
        "4 7 1 4 1 1 4 1 1 1 4 1 4 1 4",
        "4 1 4 4",
        "1 1 4 1 1 1 7",
        "4 1",
        "7 4",
        "4 7 7 4 9 4 7 7 7 4 7 7 7 9 7",
        "7 9 7 7",
        "7 10 7 4 7 10 9",
        "7 4",
        "7 7"
    ]

    index = 0
    n = int(input_data[index])
    index += 1
    name = []
    num = []
    for _ in range(n):
        parts = input_data[index].split()
        name.append(parts[0])
        if len(parts) > 1:
            num.append(float(parts[1]))
        else:
            num.append(0.0)
        index += 1

    p = [0.0] * n
    temp = 0.0
    for i in range(n):
        p[i] = 0.0
        for j in range(n):
            p[i] += num[i] / num[j]
        p[i] -= 1
        temp += p[i]

    for i in range(n):
        p[i] /= temp

    print("各类别的权重为：", end='')
    for i in range(n):
        print(f"{p[i]:.3f} ", end='')
    print()

    S = []
    for i in range(n):
        weights = [float(w) for w in input_data[index].split()]
        S.append(weights)
        index += 1

    time = int(input_data[index])
    index += 1
    t = [int(i) for i in input_data[index].split()]
    index += 1

    F = [[[0.0 for _ in range(int(num[j]))] for j in range(n)] for _ in range(len(t))]
    for k in range(len(t)):
        for j in range(n):
            values = [float(v) for v in input_data[index].split()]
            for l in range(int(num[j])):
                F[k][j][l] = values[l]
            index += 1

    H = [[0.0 for _ in range(n)] for _ in range(len(t))]
    U = [[0.0 for _ in range(n)] for _ in range(len(t))]
    T = [1.0 for _ in range(len(t))]

    for k in range(len(t)):
        for i in range(n):
            H[k][i] = 0.0
            for j in range(int(num[i])):
                H[k][i] += S[i][j] * math.log10(F[k][i][j])
            U[k][i] = max(10.0 * math.exp(-H[k][i]), 1.0)
            T[k] *= U[k][i] ** p[i]

    print("       时间    ", end='')
    for i in range(n):
        print(f"{name[i]}    ", end='')
    print()

    print("熵     ", end='')
    for k in range(len(t)):
        if k == 0:
            print(f"t={t[k]:3d}   ", end='')
        else:
            print("       t=10   ", end='')
        for i in range(n):
            print(f"{H[k][i]:.3f}  ", end='')
        print()

    print("可信度 ", end='')
    for k in range(len(t)):
        if k == 0:
            print(f"t={t[k]:3d}   ", end='')
        else:
            print("       t=10   ", end='')
        for i in range(n):
            print(f"{U[k][i]:.3f}  ", end='')
        print()
    print()

    print(" 时间             软件可信度")
    for k in range(len(t)):
        print(f"t={t[k]:3d}               {T[k]:.3f}")


if __name__ == "__main__":
    main()