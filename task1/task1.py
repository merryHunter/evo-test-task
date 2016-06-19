import random


def solve(m):
    """

    :param m:
    :return:
    """
    a_sum = []
    b_sum = []
    c_sum = []
    c = 0
    for i in m:
        for j in i:
            print j
            a_sum.append(sum(j))
            c += 1
        if c % 10 == 0:
            print ""

    print a_sum
    return [1],[1],[1]

def generate_matrix():
    return [[[random.randrange(0,10) for k in range(10)] for j in range(10)] for i in range(10)]


def main():
    m = generate_matrix()
    a, b, c = solve(m)
    print a, b, c


if __name__ == "__main__":
    main()