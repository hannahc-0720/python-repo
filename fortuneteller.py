import random

fortunes = ["You will have a successful career!", "You will go bankrupt in 20 years...", "You will have extra luck by the next full moon!", "You will soon hear good news."]

def tell_fortune():

    choice = input("Do you want a fortune?")
    if choice == "yes":
        print(random.choice(fortunes))
    elif choice == "no:":
        print("Alright. Have a nice day!")

tell_fortune()