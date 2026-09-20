def palind(r):
    e = len(r)
    s = 0
    while s < e:
        if r[s] != r[e - 1]:
            return False
        s += 1
        e -= 1
    return True

r = (1, 2, 3, 3, 2, 1)

if palind(r):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")