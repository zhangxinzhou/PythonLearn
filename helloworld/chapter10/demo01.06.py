print("\n", "=" * 10, "蚂蚁庄园动态", "+" * 10, "\n")
with open('message.txt', 'r') as file:
    message = file.read()
    print(message)
    print("\n", "=" * 10, "over", "=" * 10, "\n")
