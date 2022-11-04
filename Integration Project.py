# Logan Nguyen
# This is my integration project, which is a simple math test.

import math

print(
    "Welcome, today you are going to be taking a simple math test to prove "
    "that you have some basic math skills.")
while True:
    score = 0

    # When I was creating this question, I wanted to make it so that it
    # would count "yes" as correct either with or without capital letters.
    # After doing some research on Google, I discovered the "lower()"
    # function. https://www.geeksforgeeks.org/python-string-lower/
    pollQuestion = input("Do you like doing math? ")
    if pollQuestion.lower() == "yes":
        print("Let's get started!")
        score += 1
    else:
        print("Unfortunately, you can't take this quiz because you hate math!")
        quit()

    # I also found the quit() function while doing some research and thought
    # I'd throw it in for fun in the first question.
    # https://codeberryschool.com/blog/en/how-to-end-a-program-in-python/

    # I also found out that you can implement a scoring system.
    # https://codereview.stackexchange.com/questions/202532/python-multi-choice-quiz-with-a-score-to-count
    addition_symbol = input("What does this symbol represent? (+) ")
    if addition_symbol.lower() == "addition":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Addition (+) adds 2 numbers together.

    num1 = 6
    num2 = 2
    additionAnswer = num1 + num2
    print("What is 6 + 2? ")
    yourAnswer = int(input())
    if additionAnswer == 8:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("Does 2 + 2 = 5?")
    joke_question = input()
    joke_answer = not (2 + 2 == 5)
    if joke_question.lower() == "no" and joke_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    subtraction_symbol = input("What does this symbol represent? (-) ")
    if subtraction_symbol.lower() == "subtraction":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 9
    num2 = 5
    subtraction_answer = num1 - num2
    print("What is 9 - 5? ")
    yourAnswer = int(input())
    if subtraction_answer == 4:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Subtraction (-), subtracts 2 numbers.

    multiplication_symbol = input("What does this symbol represent? (*) ")
    if multiplication_symbol.lower() == "multiplication":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 7
    num2 = 2
    multiplication_answer = num1 * num2
    print("What is 7 * 2? ")
    yourAnswer = int(input())
    if multiplication_answer == 14:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Multiplication (*), multiplies 2 numbers together.

    division_symbol = input("What does this symbol represent? (/) ")
    if division_symbol.lower() == "division":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 10
    num2 = 2
    division_answer = num1 / num2
    print("What is 10 / 2? ")
    yourAnswer = int(input())
    if division_answer == 5:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Division (/), divides a number by another number.

    exponent_question = input("What tells you to multiply a number by itself?"
                              )
    if exponent_question.lower() == "exponent":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 4
    num2 = 2
    power_answer = num1 ** num2
    print("What is 4^2? ")
    yourAnswer = int(input())
    if power_answer == 16:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Exponent (**), is raising a number to the power of another number (
    # aka, telling you how many times to multiply a number by itself).

    quotient_question = input("What is the whole number you get when you "
                              "divide? ")
    if quotient_question.lower() == "quotient":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("What is the square root of 4?")
    square_root_answer = int(input())
    if square_root_answer == 2 or square_root_answer == -2:
        print("Correct!")
    else:
        print("Incorrect!")

    num1 = 5
    num2 = 2
    whole_number_answer = num1 // num2
    print("What is the quotient for 5/2? ")
    yourAnswer = int(input())
    if whole_number_answer == 2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Floor division, gives you the quotient when you divide 2 numbers,
    # but rounds it down to the nearest whole number.

    num1 = 9
    num2 = 4
    remainder_answer = num1 % num2
    print("What is the remainder for 9/4? ")
    your_remainder_answer = int(input())
    if remainder_answer == 1:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    # Modulus (%), gives you the remainder when you divide 2 numbers.

    num1 = 100
    num2 = 100
    equal = num1 == num2
    print("Does 100 = 100")
    equal_answer = input()
    if equal_answer.lower() == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 800
    num2 = 200
    not_equal = num1 != num2
    print("Does 800 = 200")
    not_equal_answer = input()
    if not_equal_answer.lower() == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    num1 = 500
    num2 = 300
    num3 = 90

    var = num1 > num2 and num2 > num3
    print("Is 300 less than 500 and greater than 90?")
    greater_than_answer = input()
    if greater_than_answer.lower() == "yes" and var == True:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print(
        "Calculate the radius and the area of a circle with a diameter of 10:")


    def calculateArea(radius):
        area = math.pi * radius ** 2
        return round(area, 2)


    def calculateRadius(diameter):
        radius = diameter / 2
        return radius


    correct_radius = calculateRadius(10)
    correct_area = calculateArea(correct_radius)

    user_answer_radius = int(input("Radius: "))
    user_answer_area = float(input("Area: "))

    if user_answer_radius == correct_radius:
        print("Correct!")
        score += 0.5

    else:
        print("Incorrect")

    if user_answer_area == correct_area:
        print("Correct!")
        score += 0.5

    else:
        print("Incorrect")

    print("Your score was a", format(score, ".0f") + "/18!")
    print("Thanks for taking this quiz.")
    print("If you have any questions email me, lwnguyen3410", "eagle.fgcu.edu",
          sep="@")
    print("You go have a", "awesome " * 2 + "day!")

    if score == 14:
        for x in range(3):
            print("Hooray! :)")

    else:
        print("Bummer, you didn't get all the questions correct. :(")

    go_again = input("Do you want to take the quiz again?")
    if go_again == "yes":
        break
    else:
        print("You have no choice but to take the quiz again!")
# In print statements, (+) combines 2 strings into one and (*) tells the
# program to repeat a certain string by a given number of times.
