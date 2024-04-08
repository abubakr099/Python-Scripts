# Defining Function
"""
def add(arg1,arg2):
    total = arg1 + arg2
    return total
output =add(2,3)
print(output)
print(add(10,30))
"""
"""
def adder(arg1,arg2):
    total = arg1 + arg2
    print(total)
#adder(20,30)
print(adder(20,30))
"""
"""
def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x
output = summ([1,2,3])
print(output)
"""
# Default Argument
""""
def greetings(MSG = "Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function")

greetings("Evening")
"""
#Keywords arguments
def vac_feedback(vac ,efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <=75):
        print("seems not effective , needs more trials")
    elif (efficacy > 75) and (efficacy < 90):
        print("consider the this vaccine")
    elif efficacy >=90:
        print("sure ,will take the shot.")
    else:
        print("need many more trials")
vac_feedback("pfizer",95)




