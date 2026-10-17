# problem 8: Tuples
# hackerrank: https://www.hackerrank.com/challenges/python-tuples/problem
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
