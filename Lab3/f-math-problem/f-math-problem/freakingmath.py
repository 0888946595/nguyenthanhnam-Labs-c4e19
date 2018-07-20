from random import *

def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    x = randint (1, 10)
    y = randint (1, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    res = 0
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x*y
    elif op == "/":
        res = x/y
    display_res = res + error
    
    return [x, y, op, display_res ]



def check_answer(x, y, op, display_res, user_choice):
    user_choice = ["True", "False"]
    x = randint (1, 10)
    y = randint (1, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    res = 0
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x*y
    elif op == "/":
        res = x/y
    display_res = res + error
    
        
    if error == 0:
        if user_choice == "True":
            return True
        if user_choice == "False":
                return False
        else:
            if user_choice == "True":
                return False
            if user_choice == "False":
                return True
        
        
        pass
