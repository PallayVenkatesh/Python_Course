
def findTriplet(num, ar_size):
    for i in range(0, ar_size - 2):

        for j in range(i + 1, ar_size - 1):

            for k in range(j + 1, ar_size):
                if num[i] + num[j] + num[k] == 0:
                    print("[(" ,num[i],
                          ",", num[j], ",", num[k], ")]")
                    return True

    return False


num = [1, 4, -5, 6, -4, 7]

ar_size = len(num)
findTriplet(num, ar_size)

