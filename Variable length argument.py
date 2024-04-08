#Variable Length Arguments(non-keywords argument)
import random


def oder_food(min_order ,*args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 min:")
    print("Enjoy the food party")
oder_food("salad","Pizza","burger")

#Variable length arguments with keywords arguments(**kargs)
import random
def time_activity(*args,**kwargs):
 #   print(args)
  #  print(kwargs)
    min = sum(args) + random.randint(0,60)
   # print(min)
    choice = random.choice(list(kwargs.keys()))
#    print(choice)
    print(f"YOU have to spend {min} for {kwargs[choice]}")

time_activity(10,20,10, hobby="Dance",sport="Boxing",fun="Driving",work="Devops")