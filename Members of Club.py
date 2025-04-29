f = open("Members.txt", "a")

while True:
    name = input("What is your name?")
    age = input("How old are you?")
    email = input("What is your email?")
    gender = input("What gender are you")
    
    print(f"Name: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}")
    ans = input("Would you like to confirm?").lower()[0]
    if ans == "n":
        response = input("Would you like to change:\n1.name\n2.age\n3.email\n4.gender")
        if response == "1":
            name = input("What is your name?")
        elif response == "2":
            age = input("How old are you?")
        elif response == "3":
            email = input("What is your email?")
        elif response == "4":
            gender = input("What gender are you")
    break

f.write("\n"+name+"|"+age+"|"+email+"|"+gender+"|")
f.close()