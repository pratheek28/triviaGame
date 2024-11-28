import time

global lives
lives = 3

global index
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

global points
points = 0

question = [
    "What is the largest city (in terms of population) in Europe?",
    "In what year did World War II end?",
    "What is the official language of Brazil?",
    "What is the most beautiful Math Identity?",
    "Soccer player Lionel Messi has won a record 8 Ballon D'Or's. What year did he win his first?",
    'What famous soccer player is known "Mr. UCL"?',
    "Who wrote The Iliad and The Odyssey?",
    "What is the name of the war that is associated with rising tension, but not an actual war between two superpowers?",
    "What state is said to hold the key to the White House?",
    "What is the oldest institution of higher education in the United States"
]

answers = [
    "Moscow", "Paris", "London", "Rome",
    "1943", "1944", "1945", "1946",
    "Brazilian", "Spanish", "Portuguese", "French",
    "Binomial Identity", "Euler's Identity", "Heine's Identity", "Newton's Identity",
    "2007", "2009", "2010", "2012",
    "Lionel Messi", "Andres Iniesta", "Diego Maradona", "Cristiano Ronaldo",
    "Homer", "Achilles", "Odysseus", "Sophocles",
    "Cold War", "Gulf War", "World War I", "American Civil War",
    "New York", "Pennsylvania", "Florida", "California",
    "Harvard", "Yale", "Brown", "Cornell"
]

correctAnswers = [
    "Moscow",
    "1945",
    "Portuguese",
    "Euler's Identity",
    "2009",
    "Cristiano Ronaldo",
    "Homer",
    "Cold War",
    "Pennsylvania",
    "Harvard"
]

def game(diffculty):
    global index
    global lives
    global points

    idx = 0

    if (diffculty == "easy"):
        lives = 4
        while (idx < 5):
            print()
            print(question[idx])
            print(f"1. {answers[(idx * 4)]} 2. {answers[((idx * 4) + 1)]} 3. {answers[((idx * 4) + 2)]} 4. {answers[((idx * 4) + 3)]}")
            userAnswer = str(input("Enter your answer: "))
            if userAnswer == correctAnswers[idx]:
                print("Correct!")
                correct = True
                points += 1
            else:
                print("Incorrect :(")
                lives -= 1
            if (lives == 0):
                return
            idx += 1
    elif (diffculty == "medium"):
        while (idx < 10):
            print()
            print(question[idx])
            print(
                f"1. {answers[(idx * 4)]} 2. {answers[((idx * 4) + 1)]} 3. {answers[((idx * 4) + 2)]} 4. {answers[((idx * 4) + 3)]}")
            userAnswer = str(input("Enter your answer: "))
            if userAnswer == correctAnswers[idx]:
                print("Correct!")
                correct = True
                points += 1
            else:
                print("Incorrect :(")
                lives -= 1
            if (lives == 0):
                return
            idx += 1

    else:
        lives = 1
        while (idx < 10):
            print()
            print(question[idx])
            print(
                f"1. {answers[(idx * 4)]} 2. {answers[((idx * 4) + 1)]} 3. {answers[((idx * 4) + 2)]} 4. {answers[((idx * 4) + 3)]}")
            userAnswer = str(input("Enter your answer: "))
            if userAnswer == correctAnswers[idx]:
                print("Correct!")
                correct = True
                points += 1
            else:
                print("Incorrect :(")
                lives -= 1
            if (lives == 0):
                return
            idx += 1
    return 0

def main():
    print("Hello and welcome to a trivia game!")
    time.sleep(2)
    difficulty = input("Please select your difficulty (easy, medium, or hard): ")

    while ((difficulty.lower() != "easy") and (difficulty.lower() != "medium") and (difficulty.lower() != "hard")):
        difficulty = input("Invalid selection! Please try again (easy, medium, or hard): ")

    difficulty = difficulty.lower()

    if (difficulty == "easy"):
        print("You have 4 lives. There are a total of 5 MCQ questions.")
        time.sleep(2)
        print("If you cannot get the right answer you will lose a life.")
        time.sleep(2)
        print("If you get the right answer, you will get a point.")
        time.sleep(2)
        print("Good Luck! And remember: CAPITALIZATION MATTER!!!")
        game(difficulty)
        time.sleep(2)
        print()
        print(f"Game Over! Your total points: {points}")

    elif (difficulty == "medium"):
        print("You have 3 lives. There are a total of 10 MCQ questions.")
        time.sleep(2)
        print("If you cannot get the right answer you will lose a life.")
        time.sleep(2)
        print("If you get the right answer, you will get a point.")
        time.sleep(2)
        print("Good Luck! And remember: CAPITALIZATION MATTER!!!")
        time.sleep(2)
        game(difficulty)
        print()
        print(f"Game Over! Your total points: {points}")

    else:
        print("You have 1 lives. There are a total of 10 questions.")
        time.sleep(2)
        print("If you cannot get the right answer you will lose a life.")
        time.sleep(2)
        print("If you get the right answer, you will get a point.")
        time.sleep(2)
        print("Good Luck! And remember: CAPITALIZATION MATTER!!!")
        time.sleep(2)
        print()
        game(difficulty)
        print(f"Game Over! Your total points: {points}")


if __name__ == "__main__":
    main()