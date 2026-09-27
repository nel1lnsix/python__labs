s = input()

start = 0
while not s[start].isupper():
    start += 1

digit = start + 1
while not s[digit].isdigit():
    digit += 1
step = digit + 1 - start

result = ""
for i in range(start, len(s), step):
    result += s[i]
    if s[i] == ".":
        break
print(result)
