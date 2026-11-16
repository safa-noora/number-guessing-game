import random

while True:
    number=random.randint(1,100)
    count=0

    while True:
        if count>=7:
            print(f"You Lose! The number was {number}")
            break
        try:
            guess=int(input("Guess a number between 1 and 100(7 tries):"))
        except ValueError:
            print("Enter a valid number!")
            continue
        if guess<1 or guess>100:
            print("guess a valid number in range")
            continue
        count+=1
        if number>guess:
            print("Low!")
        elif number<guess:
            print("High!")
        else:
            print(f"correct! you took {count} guesses!")
            break

    play=input("Play again(y/n)? ")
    if play.lower()!="y":
        break