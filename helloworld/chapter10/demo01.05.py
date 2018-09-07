with open('message.txt', 'r') as file:
    file.seek(10)
    string = file.read()
    print(string)
