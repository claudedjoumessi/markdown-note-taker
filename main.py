task = input("Enter your task: ")

fs = open("tasks.txt", '+a')
fs.write(task + '\n')

fs.close()