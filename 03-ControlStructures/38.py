phone_number = int(input("Enter phone number: "))
phone_number = str(phone_number)
lenght = len(phone_number)
if lenght == 9:
    print('Phone number: ',phone_number[0:3],"-",phone_number[3:6],"-",phone_number[6:9])