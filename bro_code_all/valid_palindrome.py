s = "[(]"
s1 = ""

for c in s:
    if c.isalnum():
        s1 += c.lower()
if s1 == s1[::-1]:
    print("True")
else:
    print("false")

    