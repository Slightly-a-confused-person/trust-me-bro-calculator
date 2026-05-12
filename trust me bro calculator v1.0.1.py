try:
    import math
    import time
    for i in range(3):
        print("|")
        time.sleep(1)
        print("/")
        time.sleep(1)
        print("-")
        time.sleep(1)
        print("\\")
        time.sleep(1)
    print("calculator")
    choice=input("choose an operator:\n1.Add(+)\n2.Subtract(-)\n3.Multiplication(*)\n4.Division(/)\n")
    choice2=float(input("choose number 1: "))
    choice3=float(input("choose number 2: "))
    if choice==("1"):
        print(choice2+choice3)
    elif choice==("2"):
        print(choice2-choice3)
    elif choice==("3"):
        print(choice2*choice3)
    else:
        print(choice2/choice3)
except ValueError:
    print("WHY DID YOU BREAK THE TRUST??? YOU ENTERED A NOT-NUMBER!!!")
except ZeroDivisionError:
    print("Bro. Why would you divide by zero.")
finally: print("ok, we're done here. Move on and do something more productive instead of looking at a useless calculator")