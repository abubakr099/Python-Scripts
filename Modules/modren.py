import random

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

def oder_food(min_order ,*args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 min:")
    print("Enjoy the food party")

def time_activity(*args,**kwargs):
 #   print(args)
  #  print(kwargs)
    min = sum(args) + random.randint(0,60)
   # print(min)
    choice = random.choice(list(kwargs.keys()))
#    print(choice)
    print(f"YOU have to spend {min} for {kwargs[choice]}")