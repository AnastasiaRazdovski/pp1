x = float(input("Your height in cm: "))
y = int(x//30.48)
z = round(x/2.54 - y*12)
print(f'I am {x}cm tall, i.e. {y} feet and {z} inches')