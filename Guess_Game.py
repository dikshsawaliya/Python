right_answer = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input("Guess the number: "))
    guess_count +=1
    if guess_number == right_answer:
        print("You Guessed it right !")
        break
else:
    print("Oops, You lose !!!")