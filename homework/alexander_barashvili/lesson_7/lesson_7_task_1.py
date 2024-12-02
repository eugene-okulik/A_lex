happy_number = 777

user_number = int(input("Hey buddy, try to guess the number and win a prize."
                        "\nEnter the number and test your luck ;)\n"))

while True:
    if user_number == happy_number:
        print('Oh yeah baby you did it!!!\nYou won respect!')
        break
    else:
        user_number = int(input('Try again. I believe in you!!!\n'))
