#problem 11:String Validators
# hackerrank: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    print(any(d.isalnum() for d in s))
    print(any(d.isalpha() for d in s))
    print(any(d.isdigit() for d in s))
    print(any(d.islower() for d in s))
    print(any(d.isupper() for d in s))
