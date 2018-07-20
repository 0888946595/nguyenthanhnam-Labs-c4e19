from random import randint, choice
# from evaluate import calc
import evaluate


x = randint (1, 10)
y = randint (1, 10)

op = choice(['+', '-', '*', '/'])
error = randint (-1, 1)

res = evaluate.calc(x, y, op)

display_res = res + error
print ("* "*20)
print ("{0} {1} {2} = {3}".format(x, op, y, display_res))
print ("* "*20)
ans = input ("(Y/N)? ").upper()


# if display_res == res:
#     if ans == "y":
#         print ("You Win")
#     if ans == "n":
#         print ("You Wrong")
# elif display_res != res:
#     if ans == "y":
#         print ("You Wrong")
#     if ans == "n":
#         print ("You Win")
# else:
#     print()

if error == 0:
    if ans == "Y":
        print ("Yay")
    if ans == "N":
        print ("Wrong")
else:
    if ans == "Y":
        print("Wrong")
    if ans == "N":
        print ("Yay")


