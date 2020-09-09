    
    name = input("Name: ")
    Age = input("Age: ")
    UM = input("UserName: ")

    res = ("Your name is " + name + ", you are " + Age + " years old, and your username is " + UM)
    File = open("Marios.txt", "w")
    File.write(res)
    File.close()

    print(res)
