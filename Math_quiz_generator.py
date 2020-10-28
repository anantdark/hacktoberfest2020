
import math
import random

def elementary_school_quiz(flag, n):
    '''(number,number)->(int)
     Preconditions: flag is 0 or 1, n is 1 or 2
     generates questions and returns the amount of questions that were right'''
    counter=0
    for i in range (n):
        first_number = random.randint(0,9)
        second_number= random.randint(0,9)

        if flag==0:
            print("Question "+str(i)+":")
            answer= int(input("what is the answer to "+str(first_number)+"-"+str(second_number)))
            sub=first_number-second_number
            if (answer!=sub):
                counter=counter+0
            else:
                counter=counter+1
        elif(flag==1):
            exp = (first_number)**(second_number)
            answer = int(input("what is the answer to " + str(first_number) +"^" + str(second_number)))
            if (answer!=exp):
                counter = counter + 0
            else:
                counter = counter + 1
    return counter

def high_school_quiz(a, b, c):
    '''(number,number,number)->string
        solves the root of the equation if any and returns the answer'''
    real = b ** 2 - 4 * a * c
    if (a==0 and b==0 and c==0):
        return "true"
    elif (a==0 and b==0):
        return "None"
    elif(a==0 and b!=0):
        r1=-c/b
        r2=r1
    elif (real < 0):
        complex_side = math.sqrt(-real) / (2 * a)
        r = -b / (2 * a)
        r1 = str(r) + " + i " + str(complex_side)
        r2=str(r) + " - i " + str(complex_side)
    else:
        r1=(-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        r2=(-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if(r1==r2):
        return (str(r1)+"")
    else:
        return (str(r1)+" and "+str(r2))


# main

print("***********************************************")
print("*                                             *")
print("* __welcome to my math quiz generator         *")
print("*                                             *")
print("***********************************************")

name = input("What is your name? ")

status = input(
    "Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status == '1':
    print("*********************************************************************************")
    print("*                                                                               *")
    print("* __ " + name + ", welcome to my quiz-generator for elementary school students.__        *")
    print("*                                                                               *")
    print("*********************************************************************************")

    topic=int(input("Hey "+name+"! Do you want to practice\n enter 0 for subtraction or 1 for exponentiation: "))
    if not(topic==0 or topic==1):
        print("invalid choice")
        pass
    else:
        q_index = int(input("How many questions do you want to do? Enter 0, 1 or 2: "))
        if (q_index == 0):
            print("Zero questions. Ok")
            pass
        elif (q_index==1 or q_index==2 ):
            correct=elementary_school_quiz(topic,q_index)
            if correct==q_index:
                print("Congratulations "+ name +"! You’ll probably get an A tomorrow.")
            elif correct==q_index/2:
                print("You did ok "+ name +" but I know you can do better.")
            elif correct==0:
                print("I think you need some more practice "+ name)
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")
            pass

elif status == '2':
    print("*********************************************************************************")
    print("*                                                                               *")
    print("* __ " + name + ", welcome to my quiz-generator for elementary school students.__        *")
    print("*                                                                               *")
    print("*********************************************************************************")
    # your code for welcome message
    flag = True
    while flag:
        question = input(name + ", would you like a quadratic equation solved? ")

        if question.lower().strip() != "yes":
            flag = False
        else:
            print("Good choice!")
            a = int(input("what is the co-efficient of x^2? "))
            b = int(input("what is the co-efficient of x? "))
            c = int(input("what is the constant? "))
            roots=high_school_quiz(a,b,c)
            if(roots=="true"):
                print("the equation " + str(b) + " \u22c5 x +" + str(c) + "=0 is satisfied for all numbers")
            elif (roots=="None"):
                print("the quadratic equation " + str(b) + " \u22c5 x +" + str(c) + " is satisfied for no number")
            elif (a == 0):
                print("the linear equation " + str(b) + " \u22c5 x +" + str(c) + " =0 has the following root/solution")
                print(roots)
            elif "and" not in roots:
                print("the quadratic equation "+str(a)+" \u22c5 x^2 + "+str(b)+" \u22c5 x +"+str(c)+"= 0\n has only one solution:")
                print(roots)
            else:
                print("the quadratic equation "+str(a)+" \u22c5 x^2 + "+str(b)+" \u22c5 x +"+str(c)+"= 0\n have the following roots")
                print(roots)


else:
   print("Thank you for using our program "+name)


print("Good bye " + name + "!")


