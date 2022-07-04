print("Welcome to the love calculator")

name1 = input("What is your name?\n").lower()
name2 = input("what is your patner's name?\n").lower()

number1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count(
    "e") + name2.count("t") + name2.count("r") + name2.count(
        "u") + name2.count("e")

number2 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count(
    "e") + name2.count("l") + name2.count("o") + name2.count(
        "v") + name2.count("e")
totals = str(number1) + str(number2)
total = int(totals)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif total >= 40 and total <= 50:
    print(f"Your score is {total},you are alright together")
else:
    print(f"Your score is {total}")
