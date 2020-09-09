#input testing

function input(prompt)
    print(prompt)
        readline()
    end

name = input("Name: ")
age = parse(Int, input("Age: "))
user_name = input("Username: ")

print(string("Your name is ", name, ", you are ", age,
    " years old, and your username is ", user_name, "."))
