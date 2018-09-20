user = input ('Whats your user name? ')

age = int(input ('Whats your age? '))

login = user + str(age)

if age < 18:
    print("Your are denied")
else:
    print("accepted")


print (login)
