# task = input("Enter your task: ")

# fs = open("tasks.txt", '+a')
# fs.write(task + '\n')

# fs.close()

def app():
    # show_menu()
    show_tasks()

# Subroutine
# To read all tasks
def show_tasks():
    fs = open("tasks.txt")
    data = fs.read()
    fs.close()
    
    print(data)

# Renders a menu 
def show_menu():
    actions = [
        "Add a task",
        "Read all tasks",
        "Modify a task",
        "Quit"
    ]
    ac = 0 # Init an action count
    for action in actions:
        ac += 1
        print(f"{ac}. {action}")
        
# Execute app
app()