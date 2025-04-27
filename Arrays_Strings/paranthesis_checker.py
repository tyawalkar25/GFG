s = '}}}}'

stack = []
count = 0
close_count = 0
for i in range(len(s)):
    if (s[i] == '(' or s[i] == '{' or s[i] == '['):
        stack.append(s[i])
            
    else:
        if stack and ((stack[-1] == '(' and s[i] == ')') or (stack[-1] == '[' and s[i] == ']') or (stack[-1] == '{' and s[i] == '}')):
            stack.pop()
            count += 1

    if(s[i] == ')' or s[i] == ']' or s[i] == '}'):
        close_count += 1

#print(close_count)
if len(stack) == 0 and count > 0 and count == close_count:
    print('true')
else:
    print('false')
