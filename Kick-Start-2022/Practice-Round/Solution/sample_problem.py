# Sample Problem
# N bags of candy
# M kids distribute
# i-th bags - C piecies
# Each kid recieves same amount of candy
# Remaining pieces of candy


def candy(M, C):
    return C % M


def main():
    T = int(input())  # Number of test cases
    C, O = [], []
    for i in range(1, T + 1):
        N, M = [int(S) for S in input().split(" ")]
        C = sum([int(S) for S in input().split(" ")])
        print("Case #{}: {}".format(i, candy(M, C)))


if __name__ == "__main__":
    main()
