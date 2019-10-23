import os


def check(ll):
    # check if the list is sorted
    bord_end = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

    while ll != bord_end:
        return False


def print_bord(ll):
    os.system("cls")  # for windows you need to use "cls" instead of "clear"
    # print("15\t14\t13\t12\n11\t10\t9\t8\n7\t6\t5\t4\n3\t1\t2\t_")
    for i in range(len(ll)):
        if i % 4 == 0:  # and i != 0:
            print()
        if bord[i] != 0:
            print(bord[i], end='\t')
        else:
            print(" ", end="\t")
    print()


def check_move(move, bb):
    # number_0 = bb.index(0)
    # move = bb.index(move)
    if bb.index(move) == bb.index(0) + 1 \
            or bb.index(move) == bb.index(0) - 1 \
            or bb.index(move) == bb.index(0) + 4 \
            or bb.index(move) == bb.index(0) - 4:
        index_0 = bb.index(0)
        index_move = bb.index(move)
        bb[index_0], bb[index_move] = bb[index_move], bb[index_0]
        # bb.index(0), bb.index(move) = bb.index(move), bb.index(0)
        return bb


if __name__ == "__main__":
    print("You are playing the 15-th game")
    # bord = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0, 14, 15]
    bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]
    while not check(bord):
        print_bord(bord)
        while True:
            your_try = int(input("Enter numb 1-15 >>"))
            if check_move(your_try, bord):
                print(bord)
                break
