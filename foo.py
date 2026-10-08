number = input("what is your credit card number?\n\n")
with open("card_number.txt", "w") as file:
    file.write(number)