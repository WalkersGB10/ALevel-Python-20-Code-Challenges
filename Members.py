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

f.write(name+"|"+age+"|"+email+"|"+gender+"|")
f.close()

ans = input("Would you like to see members?").lower()
if ans[0] == "y":
    f = open("Members.txt", "r")
    stuff = f.read()
    f.close()
    members = stuff.split("|")
    print(members)
    person = input("Who would you like to find")
    if person in members:
        pos = members.index(person)
        name = members[pos]; age = members[pos+1]; email = members[pos+2]; gender = members[pos+3]
        print(f"Name: {name}\nAge: {age}\nEmail: {email}\nGender: {gender}")
    else:
        print(person, "not in club")
