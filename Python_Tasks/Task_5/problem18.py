# problem 18: The Minion Game
# hackerrank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
  vowels = 'AEIOU'
  s_score = 0
  k_score = 0
  n = len(string)
  for i in range(n):
    if string[i] in vowels:
      k_score += n - i
    else:
      s_score += n - i
  if s_score > k_score:
    print(f'Stuart {s_score}')
  elif k_score > s_score:
    print(f'Kevin {k_score}')
  else:
    print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
