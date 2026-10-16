# 1 
def freq(sentence):
    
    words = sentence.lower().split()
    s = {}
    for word in words:
        if word in s:
            s[word] +=1

        else:
            s[word] = 1
    return s
sentence = "python is easy and python is powerful"
r = freq(sentence)
print(r)
print()
sentence = "data analysis is data visualization, data cleaning and data processing"
e = freq(sentence)
print(e)

#2
def ch_freq(word):
    d = {}
    for char in word:
        if char in d:
            d[char] +=1 
        else:
            d[char] = 1
    return d
word = "banana"
w = ch_freq(word)
print(w)
print()
word = "python"
d = ch_freq(word)
print(d)

#3
def non_repeat(word):
    for char in word:
        if word.count(char) ==1:
            return char
    return None
word = "swiss"
p = non_repeat(word)
print(p)
print()
word = "lalalala"
q = non_repeat(word)
print(q)

#4 
def ana(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")
    if len(s1)!=len(s2):
        return False
    for char in s1:
        if s1.count(char)!=s2.count(char):
            return False
    return True
s1 = "listen"
s2 = "silent"
s = ana(s1,s2)
print(s)
print()
s1 = "rack"
s2 = "car"
s = ana(s1,s2)
print(s)

#5
def fr(word):
    g = []
    for char in word:
        if char in g:
            return char
        else:
            g.append(char)
    return None
word = "programming"
e = fr(word)
print(e)
print()
word = "games"
w = fr(word)
print(w)

#6 
def zeros(li):
    w = []
    for l in li:
        if l!=0:
            w.append(li)
    count = len(li) - len(w)
    for i in range(count):
        w.append(0)
    return w
li = [0, 3, 0, 1, 2, 0, 4]
e = zeros(li)
print(e)
print()
li = [0,1,3,0,0,0,2]
q = zeros(li)
print(q)

#7 
def sh(n):
    u = []
    for i in n:
        if i not in u:
            u.append(i)
    if len(u)<2:
        return None
    u.sort()
    return u[-2]
n = [10, 20, 40, 30, 40, 20]
w = sh(n)
print(w)
print()
n = [23,11,568,-21,4,0]
d = sh(n)
print(d)

#8 
def dups(n):
    e = []
    for i in n:
        if i not in e:
            e.append(i)
    return e
n = [4, 2, 4, 5, 2, 7, 5]
l = dups(n)
print(l)
print()
n = [5,1,2,-2,0]
p = dups(n)
print(p)

#9 

def missing(n,m):
    total = m*(m+1)//2
    sum = 0
    for i in n:
        sum = sum+i
    miss = total-sum
    return miss
n = [1,2,4,5,6]
m = 6
l = missing(n,m)
print(l)
print()
n = [1,2,3,4,5,6]
m = 7
b = missing(n,m)
print(b)

#10
def find(n,target):
    for j in range(1,len(n)):
        for i in range(j):
            if n[i]+n[j] == target:
                return [n[i],n[j]]
    return []
n = [2, 7, 11, 15]
target = 9
d = find(n,target)
print(d)
print()
n = [1,2,3,4,0]
target = 2
x = find(n,target)
print(x)

#11
def close(n):
    if len(n)==0:
        return None
    closest = n[0]
    for i in n:
        if abs(i)<abs(closest):
            closest = i
        elif abs(i) == abs(closest) and i>closest:
            closest=n
    return closest
n = [-8, -3, 2, 5, -2]
j = close(n)
print(j)
print()
n = [2,1,0,-1,8]
g = close(n)
print(g)

#12
def common(list1,list2):
    d = []
    for i in list1:
        if i in list2 and i not in d:
            d.append(i)
    return d
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
v = common(list1,list2)
print(v)
print()
list1 = [3,7,0,8]
list2 = [2,6]
f = common(list1,list2)
print(f)

#13
def rotate(n,k):
    if len(n)==0:
        return []
    k=k%len(n)
    if k!=0:
        r = n[-k:]+n[:-k]
    else:
        n[:] 
    return r
n = [1, 2, 3, 4, 5]
k = 2
h = rotate(n,k)
print(h)
print()
n = [1,1,2,2,3]
k = 7
d = rotate(n,k)
print(d)

#14
def max(n):
    max_sum = n[0]+n[1]
    for i in range(1,len(n)-1):
        sum = n[i]+n[i+1]
        if sum > max_sum:
            max_sum = sum
    return max_sum
n = [4, 7, 2, 9, 5]
e = max(n)
print(e)
print()
n = [3,1,-2,0]
s = max(n)
print(s)

#15
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
n= [2, 4, 3, 5, 7, 8, 1]
target = 9
b = pairs(n,target)
print(b)
print()
n= [0,1,-2,9,6,3,4,7,22]
target = 7
k = pairs(n,target)
print(k)

