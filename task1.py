import random


def solve(m):
    """

    :param m:
    :return:
    """
   

def generate_matrix():
    return [[[random.randrange(0,10) for k in range(10)] for j in range(10)] for i in range(10)]


def main():
    m = generate_matrix()
    a, b, c = solve(m)
    print a, b, c


if __name__ == "__main__":
    main()