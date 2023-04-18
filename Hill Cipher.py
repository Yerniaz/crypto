n = int(input("Enter the size of key matrix: "))
print("Enter the key matrix:")
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

s = input("Enter the message to encrypt: ")
temp = (n - len(s) % n) % n
s += 'x' * temp

k = 0
ans = ""
while k < len(s):
    for i in range(n):
        sum = 0
        temp = k
        for j in range(n):
            sum += (a[i][j] % 26 * (ord(s[temp]) - ord('a')) % 26) % 26
            sum = sum % 26
            temp += 1
        ans += chr(sum + ord('a'))
    k += n

print(ans)
