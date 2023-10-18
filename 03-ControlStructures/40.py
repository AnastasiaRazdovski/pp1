card_number = int(input("Enter credit card number: "))
card_number = str(card_number)
lenght = len(card_number)
if lenght == 16:
    print('card number: ',card_number[0:4], " " ,card_number[4:8], " " ,card_number[8:12], " " ,card_number[12:16])