s = "[()]("
stack = []
closetopen = { ")" : "(", "]" : "[", "}" : "{"}

for c in s:
    if c in closetopen:
        if stack and stack[-1] == closetopen[c]:
            stack.pop()
        else:
            print("false")
    else:
        stack.append(c)
# return True if not stack else False
print("True" if not stack else "False")

