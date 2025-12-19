
# fs = open("tasks.txt", '+a')
# fs.write(task + '\n')

# fs.close()

def app():
    while True:
        show_menu()
        action = input('Enter an option to continue: ')
        match action:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
    
    show_tasks()

# Subroutines

# Get tasks
def get_tasks():
    fs = open("tasks.txt")
    data = fs.read()
    fs.close()
    
    return data

def write_tasks(tasks):
    fs = open("tasks.txt", "w")
    fs.write(tasks.join('\n'))

# To read all tasks
def show_tasks():
    print(get_tasks())

# To add a task
def add_task(task):
    # 1. Grab data and append...
    tasksAdded = get_tasks() + task
    # ...to file database
    write_tasks(tasksAdded)

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