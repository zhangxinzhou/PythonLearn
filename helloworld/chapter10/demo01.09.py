print("\n", "=" * 35, "蚂蚁庄园动态", "=" * 35, "\n")
with open('message.txt', 'r') as file:
    messageall = file.readlines()
    for message in messageall:
        print(message)
print("\n", "=" * 35, "over", "=" * 35, "\n")
