phone_directory = {
    "Amal": "1111111111",
    "Mohammed": "2222222222",
    "Khadijah": "3333333333",
    "Abdullah": "4444444444",
    "Rawan": "5555555555",
    "Faisal": "6666666666",
    "Layla": "7777777777"
}

user_input = input("Enter a phone number: ")

if not user_input.isdigit() or len(user_input) != 10:
    print("This is an invalid number.")
else:
    name = phone_directory.get(user_input, None)

    if name:
        print("Name:", name)
    else:
        print("Sorry, the number is not found.")