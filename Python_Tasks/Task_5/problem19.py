# problem 19 : Merge the Tools!
# hackerrank: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        unique = dict.fromkeys(substring)
        print("".join(unique))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
