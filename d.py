def reverse(x):
    stringed = str(x)
    digits = len(stringed)
    backwards = 0
    status = False
    if stringed[0] == '-':
        stringed = stringed[1:]
        status = True
        digits = digits - 1
    for i in range(0, digits):
        y = x % 10
        backwards = backwards * 10 + y
        x = (x - y) / 10
    if status:
        return int(-1 * backwards)
    return int(backwards)
print(reverse(-123))