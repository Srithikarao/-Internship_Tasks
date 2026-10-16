# Q1. Find the Frequency of Each Word in a Sentence
# Write a Python program to count how many times each word appears in a given sentence and store the result in a dictionary.
# Example Input:
# python is easy and python is powerful
# Expected Output:
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

def freq(sentence):
    words = sentence.lower().split()
    s = {}
    for word in words:
        if word in s:
            s[word] +=1

        else:
            s[word] = 1
    return s

    
#   Q2. Find the Frequency of Each Character in a Word
# Write a Python program to count how many times each character appears in a given word and store the result in a dictionary.
# Example Input:
# banana
# Expected Output:
# {'b': 1, 'a': 3, 'n': 2}
      
def ch_freq(word):
    d = {}
    for char in word:
        if char in d:
            d[char] +=1 
        else:
            d[char] = 1
    return d

# Q3. Find the First Non-Repeating Character in a Word
# Write a Python program to find the first character that appears only once in a given word. If no such character exists, return None.
# Example Input:
# swiss
# Expected Output:
# w

def non_repeat(word):
    for char in word:
        if word.count(char) ==1:
            return char
    return None

# Q4. Check Whether Two Strings Are Anagrams
# Write a Python program to check whether two strings are anagrams.
# Two strings are anagrams if they contain the same characters with the same frequencies, regardless of their order.
# Example Input:
# s1 = "listen"
# s2 = "silent"
# Expected Output:
# True

def ana(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
    if len(s1)!=len(s2):
        return False
    for char in s1:
        if s1.count(char)!=s2.count(char):
            return False
    return True

# Q5. Find the First Repeating Character in a String
# Write a Python program to find the first character whose second occurrence is encountered while reading the string from left to right.
# If no character repeats, return None.
# Example Input:
# programming
# Expected Output:
# r

def fr(word):
    g = []
    for char in word:
        if char in g:
            return char
        else:
            g.append(char)
    return None

# Q6. Move All Zeros to the End of a List
# Write a Python program to move all zeros to the end of a list while maintaining the original order of non-zero elements.
# Example Input:
# [0, 3, 0, 1, 2, 0, 4]
# Expected Output:
# [3, 1, 2, 4, 0, 0, 0]

def zeros(li):
    w = []
    for i in li:
        if i!=0:
            w.append(li)
    count = len(li) - len(w)
    for j in range(count):
        w.append(0)
    return w

# Q7. Find the Second Highest Distinct Number in a List
# Write a Python program to find the second-largest distinct number in a given list.
# Duplicate values should not be considered separate ranks.
# If a second distinct number does not exist, return None.
# Example Input:
# [10, 20, 40, 30, 40, 20]
# Expected Output:
# 30

def sh(n):
    u = []
    for i in n:
        if i not in u:
            u.append(n)
    if len(u)<2:
        return None
    u.sort()
    return u[-2]

# Q8. Remove Duplicates Without Changing the Original Order
# Write a Python program to remove duplicate elements from a list while preserving the order of their first occurrence.
# Example Input:
# [4, 2, 4, 5, 2, 7, 5]
# Expected Output:
# [4, 2, 5, 7]

def dups(n):
    e = []
    for i in n:
        if i not in e:
            e.append(i)
    return e

# Q9. Find the Missing Number from 1 to N
# Write a Python program to find the missing number in a list containing numbers from 1 to N.
# The list contains exactly one missing number, and all remaining numbers appear only once.
# Example Input:
# nums = [1, 2, 4, 5, 6]
# N = 6
# Expected Output:
# 3

def missing(n,m):
    total = n*(n+1)//2
    sum = 0
    for i in n:
        sum = sum+n
    miss = total-sum
    return miss

# Q10. Find Two Numbers Whose Sum Equals a Target
# Write a Python program to find the first pair of numbers whose sum equals a given target.
# Return the pair as a list. If no valid pair exists, return an empty list.
# Return the pair whose second element is encountered earliest when scanning the input from left to right. If multiple earlier elements qualify, choose the earliest one.
# Example Input:
# nums = [2, 7, 11, 15]
# target = 9
# Expected Output:
# [2, 7]

def find(n,target):
    for j in range(len(n)):
        for i in range(j):
            if n[i]+n[j] == target:
                return [n[i],n[j]]
    return []

# Q11. Find the Number Closest to Zero
# Write a Python program to find the number closest to zero in a given list.
# If two numbers are equally close to zero, return the positive number.
# Example Input:
# [-8, -3, 2, 5, -2]
# Expected Output:
# 2

def close(n):
    if len(n)==0:
        return None
    closest = n[0]
    for i in n:
        if abs(n)<abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i>closest:
            closest=n
    return closest

#   Q12. Find Common Elements Between Two Lists
# Write a Python program to find the common elements between two lists.
# Each common element should appear only once in the result, maintaining the order of its first occurrence in the first list.
# Example Input:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Expected Output:
# [3, 4, 5]
  
def common(list1,list2):
    d = []
    for i in list1:
        if i in list2 and i not in d:
            d.append(i)
    return d

# Q13. Rotate a List to the Right by K Positions
# Write a Python program to rotate the elements of a list to the right by K positions.
# Elements shifted beyond the last position should move to the beginning of the list.
# Example Input:
# nums = [1, 2, 3, 4, 5]
# K = 2
# Expected Output:
# [4, 5, 1, 2, 3]

def rotate(n,k):
    if len(n)==0:
        return []
    k=k%len(n)
    if k!=0:
        r = n[-k:]+n[:-k]
    else:
        n[:] 
    return r


# Q14. Find the Maximum Sum of Two Consecutive Elements
# Write a Python program to find the maximum sum of any two consecutive elements in a list.
# Assume the list contains at least two elements.
# Example Input:
# [4, 7, 2, 9, 5]
# Expected Output:
# 14

def max(n):
    max_sum = n[0]+n[1]
    for i in range(1,len(n)-1):
        sum = n[i]+n[i+1]
        if sum > max_sum:
            max_sum = sum
    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
# Write a Python program to find all unique pairs of numbers whose sum equals a given target.
# Each pair should contain two distinct list positions, and duplicate pairs should not be included.
# Return each pair in ascending numerical order. Return the list of pairs sorted by their first element. If no valid pairs exist, return an empty list.
# Example Input:
# nums = [2, 4, 3, 5, 7, 8, 1]
# target = 9
# Expected Output:
# [[1, 8], [2, 7], [4, 5]]

def pairs(n,target):
    r = []
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]+n[j]==target:
                pair = [n[i],n[j]]
                pair.sort()
                if pair not in r:
                    r.append(pair)
    r.sort()
    return r


