# BOJ 10808번
s = input()

alpha = [0] * 26

for i in range(len(s)):
    j = ord(s[i]) - ord("a")
    alpha[j] += 1

for i in range(26):
    print(alpha[i], end=" ")