aa = [[0 for x in range(42)] for y in range(42)]
a = [[0 for x in range(42)] for y in range(42)]
version = 0
z = 0
sum = 0


def solve1(out):
    global version
    num1 = 0
    num2 = 0
    num3 = 0
    z = 256
    for i in range(34, 37):
        for j in range(39, 42):
            if a[i][j] != 0:
                num1 = num1 + z
            z = z / 2
    z = 256
    for i in range(39, 42):
        for j in range(34, 37):
            if a[i][j] != 0:
                num2 += z
            z = z / 2
    for i in range(39, 42):
        for j in range(39, 42):
            if a[i][j] != 0:
                num3 += z
            z = z / 2
    if num1 == num2 and num2 == num3:
        out.write(str(num1) + "\n")
        version = num1
        return True
    out.write(str(0) + "\n")
    return False


def solve2_1(x, y, out, vout):
    if (((1 ^ a[x][y] ^ a[x][y + 1] ^ a[x][y + 2] ^ a[x][y + 3]) == a[x][y + 4]) and (
            (1 ^ a[x + 1][y] ^ a[x + 1][y + 1] ^ a[x + 1][y + 2] ^ a[x + 1][y + 3]) == a[x + 1][y + 4])):
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
                z = z / 2
        c = sum
        out.write(c)
        vout.write(1)
    else:
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
            z = z / 2
        c = sum
        out.write(c)
        vout.write(0)


def solve2(out, vout):
    i = 1
    while i <= 5:
        j = 9
        while j <= 29:
            solve2_1(i, j, out, vout)
            solve2_1(i + 2, j, out, vout)
            j = j + 5
        i = i + 4


def solve3_1(x, y, out, vout):
    if (((1 ^ a[x][y] ^ a[x + 1][y] ^ a[x + 2][y] ^ a[x + 3][y]) == a[x + 4][y]) and
            ((1 ^ a[x][y + 1] ^ a[x + 1][y + 1] ^ a[x + 2][y + 1] ^ a[x + 3][y + 1]) == a[x + 4][y + 1]) and
            ((1 ^ a[x][y + 2] ^ a[x + 1][y + 2] ^ a[x + 2][y + 2] ^ a[x + 3][y + 2]) == a[x + 4][y + 2]) and
            ((1 ^ a[x][y + 3] ^ a[x + 1][y + 3] ^ a[x + 2][y + 3] ^ a[x + 3][y + 3]) == a[x + 4][y + 3])):
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
                z = z / 2
        c = sum
        out.write(c)
        vout.write(1)
        z = 128
        sum = 0
        for i in range(2, 4):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
        c = sum
        out.write(c)
        vout.write(1)
    else:
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
            z = z / 2
        c = sum
        out.write(c)
        vout.write(1)
        for i in range(2, 4):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
            z = z / 2
        c = sum
        out.write(c)
        vout.write(0)


def solve3(out, vout):
    i = 9
    while i <= 29:
        j = 1
        while j <= 5:
            solve3_1(i, j, out, vout)
            j = j + 4
        i = i + 5


def solve4_1(x, y, out, vout):
    if ((1 ^ a[x][y] ^ a[x][y + 1] ^ a[x][y + 2] ^ a[x][y + 3]) == a[x][y + 4]) and (
            (1 ^ a[x + 1][y] ^ a[x + 1][y + 1] ^ a[x + 1][y + 2] ^ a[x + 1][y + 3]) == a[x + 1][y + 4]) and (
            (1 ^ a[x][y] ^ a[x + 1][y] ^ a[x + 2][y] ^ a[x + 3][y]) == a[x + 4][y]) and (
            (1 ^ a[x][y + 1] ^ a[x + 1][y + 1] ^ a[x + 2][y + 1] ^ a[x + 3][y + 1]) == a[x + 4][y + 1]) and (
            (1 ^ a[x][y + 2] ^ a[x + 1][y + 2] ^ a[x + 2][y + 2] ^ a[x + 3][y + 2]) == a[x + 4][y + 2]) and (
            (1 ^ a[x][y + 3] ^ a[x + 1][y + 3] ^ a[x + 2][y + 3] ^ a[x + 3][y + 3]) == a[x + 4][y + 3]):
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
                z = z / 2
        c = sum
        out.write(c)
        vout.write(1)
        z = 128
        sum = 0
        for i in range(2, 4):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
        c = sum
        out.write(c)
        vout.write(1)
    else:
        z = 128
        sum = 0
        for i in range(0, 2):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
            z = z / 2
        c = sum
        out.write(c)
        vout.write(1)
        for i in range(2, 4):
            for j in range(0, 4):
                if a[x + i][y + j] != 0:
                    sum = sum + z
            z = z / 2
        c = sum
        out.write(c)
        vout.write(0)


def solve4(out, vout):
    i = 9
    while i <= 29:
        j = 9
        while j <= 29:
            solve4_1(i, j, out, vout)
            j = j + 5
        i = i + 5


def solve5(out, vout):
    i = 9
    while i <= 29:
        j = 34
        while j <= 38:
            solve3_1(i, j, out, vout)
            j = j + 4
        i = i + 5


def solve6(out, vout):
    i = 34
    while i <= 38:
        j = 9
        while j <= 29:
            solve2_1(i, j, out, vout)
            solve2_1(i + 2, j, out, vout)
            j = j + 5
        i = i + 4


if __name__ == '__main__':
    IN = open("C:\\Users\\Lenovo1\\Desktop\\001.txt", "rb")
    out = open("C:\\Users\\Lenovo1\\Desktop\\out.bin", "wb")
    vout = open("C:\\Users\\Lenovo1\\Desktop\\vout.bin", "wb")
    x = IN.read().split(" ")
    for i in range(1, 42):
        for j in range(1, 42):
            a[i][j] = int(x[i][j])
    if solve1(out):
        solve2(out, vout)
        solve3(out, vout)
        solve4(out, vout)
        solve5(out, vout)
        solve6(out, vout)
    else:
        for i in range(1, 131):
            out.write(bytes(0))
            vout.write(bytes(0))
    IN.close()
    out.close()
    vout.close()
