# task = input("Enter your task: ")

# fs = open("tasks.txt", '+a')
# fs.write(task + '\n')

# fs.close()

def app():
    # show_menu()
    show_tasks()

# Subroutines

# Get tasks
def get_tasks():
    fs = open("tasks.txt")
    data = fs.read()
    fs.close()
    
    return data

# To read all tasks
def show_tasks():
    print(get_tasks())

# To add a task
def add_task(task):
    # 1. Grab data
    tasksAdded = get_tasks() + task
    return tasksAdded

# To modify a task
# Returns the new tasks array
def modify_task(id, newStr):
    tasks = get_tasks()
    tasksArr = tasks.split()
    
    tasksArr[id] = newStr
    return tasksArr

def delete_task(id):
    tasksArr = get_tasks().split()
    tasksArr.__delitem__(id)
    
    return tasksArr

# Renders a menu 
def show_menu():
    actions = [
        "Add a task",
        "Read all tasks",
        "Modify a task",
        "Delete a task",
        "Quit"
    ]
    ac = 0 # Init an action count
    for action in actions:
        ac += 1
        print(f"{ac}. {action}")
        
# Execute app
app()