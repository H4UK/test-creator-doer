import csv
import random


def addToAll(string11):
    string11 = string11[:-4]
    with open("all.csv", mode='a', newline="") as csvfile:
        fieldnames = ['Name', "Number"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"Name": string11, "Number": "1"})


def createquiz():
    print("Proceeding to create quiz...")
    inte = random.randint(1, 1000)
    string = input("Name your file: ")
    string2 = ".csv"
    string = string + str(inte) + string2
    number_of_questions = input("How much questions would you like?\n")
    while True:
        try:
            number_of_questions = int(number_of_questions)
            break
        except ValueError as error:
            print("You can't do that, we need an integer")
            return False
    with open(string, 'w', newline="") as csvfile:
        fieldnames = ['Question', 'Answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(number_of_questions):
            string3 = input("Name A question: ")
            string3 = string3 + " "
            string4 = input("Name the answer for the question: ")

            writer.writerow({"Question": string3, "Answer": string4})
    print("Your file name is called: ", string)
    addToAll(string)

    print("Thank you, restart program to see if your new test got added to my dictionary!")


def start():
    yesorno = input("Do you want to play an existing quiz(1) or create one?(2)\n(1) or (2)\nANS: ")
    if yesorno == "1":
        with open('all.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            filenames = " "
            for line in csv_reader:
                filenames = filenames + line[0] + ", "
            filenames = filenames[:-2]
            filenames = filenames.strip()
            if len(filenames) == 0:
                print("Restart and Create a Quiz")
            if len(filenames) >= 1:
                print("Procceding to start quiz!")
                print("The quizzes that exists ")
                print("-", filenames, "-")
                which_qna_please = input("Which QnA do you want to do?\nANS: ")
                print("Your quiz: ")
                print(which_qna_please)
                test(which_qna_please)
    elif yesorno == "2":
        createquiz()
        x = 0
    else:
        print("1,2, not that hard. I'm not going to do anything bye!!")
        x = 0


def test(filename):
    print(
        "Disclaimer:\nThis program is case sensitive,\njust make sure you don't add spaces and accidental mistakes\n\n")
    score = 0
    full = 0
    filename = filename + ".csv"
    try:
        with open(filename, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                answer = input(line[0])
                if answer == line[1]:
                    print('Correct answer!\n')
                    score += 1
                    full += 1
                else:
                    print('Incorrect, the answer is: ', line[1], '\n')
                    full += 1
            # if score/full <= .50:
            #    print("Restart now lol, you got", score/full)
            # if score/full >= 50:
            num = score / full

            dec_num = num * 100
            if round(dec_num, 0) < 50:
                print("Congrats!!! YOU FAILED, you scored ", round(dec_num, 0), "!!!")
            if round(dec_num, 0) > 51:
                print("Congrats!!! YOU PASSED, you scored ", round(dec_num, 0), "!!!")
    except FileNotFoundError as fnferror:
        print("\n\n\n\nRestart, there are no files named\n", filename, "\n\n\n\n\n")
