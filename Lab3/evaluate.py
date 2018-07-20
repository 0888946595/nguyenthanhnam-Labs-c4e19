# Định nghĩa Function
# Function Argument (Tham số đầu vào)
def calc(x, op, y):
    res = 0
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x*y
    elif op == "/":
        res = x/y

    return res


# Gọi Function
    # res = calc(1, "-" ,3)

    # print (res)

