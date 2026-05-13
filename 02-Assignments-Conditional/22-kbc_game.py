# 23.Create Your Own KBC Game 

ask_usr = input("Would You Like the Start Game ?(start/not) : ")
points = 0
c_ans = 0
w_ans = 0

if ask_usr == "start":
    print("------Let's Proceed.------")
    print("""
        1. Who developed Python Programming Language?
        A. Wick van Rossum
        B. Rasmus Lerdorf
        C. Guido van Rossum
        D. Niene Stom
    """)
    ans1 = input("   Ans :- ")
    if ans1 == "C":
        print("     Correct Answer !")
        points = points + 1000
        c_ans = c_ans + 1
    else:
        print("incorrect answers, no points will be awarded.!")
        w_ans = w_ans + 1

    print("""
        2.Which of the following character is used to give single-line comments in Python?
        A. //
        B. #
        C. !
        D. /* 
    """)
    ans2 = input("   Ans :- ")
    if ans2 == "B":
        print("     Correct Answer !")
        points = points + 2000
        c_ans = c_ans + 1
    else:
        print("incorrect answers, no points will be awarded.!")
        w_ans = w_ans + 1

    print("""
        3.Which of the following functions is a built-in function in python?
        A. factorial()
        B. print()
        C. seed()
        D. sqrt()
    """)
    ans3 = input("   Ans :- ")
    if ans3 == "B":
        print("     Correct Answer !")
        points = points + 3000
        c_ans = c_ans + 1
    else:
        print("incorrect answers, no points will be awarded.!")
        w_ans = w_ans + 1

    print("""
        4. What is the return type of the id() function in Python?
        A. int
        B. float
        C. bool
        D. dict
    """)
    ans4 = input("   Ans :- ")
    if ans4 == "A":
        print("     Correct Answer !")
        points = points + 5000
        c_ans = c_ans + 1
    else:
        print("incorrect answers, no points will be awarded.!")
        w_ans = w_ans + 1

    print("""
        5.Which keyword is used for function in Python language?
        A. Function
        B. def
        C. Fun
        D. Define
    """)
    ans5 = input("   Ans :- ")
    if ans5 == "B":
        print("     Correct Answer !")
        points = points + 10000
        c_ans = c_ans + 1
    else:
        print("incorrect answers, no points will be awarded.!")
        w_ans = w_ans + 1

    print(f"Total Score of Correct Answers : {points}")
    print(f"Number of correct answers : {c_ans}")
    print(f"Number of Wrong answers : {w_ans}")

elif ask_usr == "not":
    print("Ok, We will start Next Time.")
else:
    print("I didn't Understand What You Said")