x = int(input("x = "))
operation = input("Operation(+,-,*,/): ")
y = int(input("y = "))


# if operation == "+":
#     tong = x + y
#     print (tong)
# elif operation == "-":
#     tong = x-y
#     print (tong)
# elif operation == "*":
#     tong = x*y
#     print (tong)
# elif operation == "/":
#     tong = x/y
#     print (tong)

                                    # bai chua
res = 0
if operation == "+":
    res = x + y
elif operation == "-":
    res = x - y
elif operation == "*":
    res = x*y
elif operation == "/":
    res == x/y

print ("{0} {1} {2} = {3}".format(x, operation, y, res))
    