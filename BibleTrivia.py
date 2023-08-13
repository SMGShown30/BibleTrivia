print("Welcome To Bible Trivia")
print("Enter Your Name Here:")
name = input()
print("Hello " + name + "!!!")
print("We will begin with the quiz!")
print("You will need to chose the difficulty.  Easy or Hard")

right = 0
wrong = 0

difficulty = input()
if difficulty == "Easy" or difficulty == "easy":
    print("You have chosen easy mode.")
    print("Question 1: How many days did it rain while Noah on the ark?")
    ans1 = input()
    if ans1 == "40":
        print("Correct.")
        right += 1
    else:
        print("Incorrect.")
        wrong += 1
    print("Question 2: How old was Jesus when he died?")
    ans2 = input()
    if ans2 == "33":
        print("Correct")
        right += 1
    else:
        print("Incorrect")
        wrong += 1
    print("Last question")
    print("Question 3: What is the name of the 1st king of Israel?")
    ans3 = input()
    if ans3 == "King Saul" or ans3 == "Saul":
        print("Correct")
        right += 1
    else:
        print("Incorrect")
        wrong += 1
else:
    print("You have chosen hard mode.")
    print("Question 1: How many generations were there from Adam to Jesus?")
    ans4 = input()
    if ans4 == "42":
        print("Correct")
        right += 1
    else:
        print("Incorrect")
        wrong += 1
    print("Question 2: Who wrote the book of Acts?")
    ans5 = input()
    if ans5 == "Paul" or ans5 == "paul":
        print("Correct")
        right += 1
    else:
        print("Incorrect")
        wrong += 1
    print("Last question")
    print("Question 3: What is the name of the high priest during the time of Jesus?")
    ans6 = input()
    if ans6 == "Caiaphas" or ans6 == "caiaphas":
        print("Correct")
        right += 1
    else:
        print("Incorrect")
        wrong += 1

print("Your final score is " + str(right) + " questions correct and " + str(wrong) + " questions incorrect.")
print("Thanks for playing!!!")