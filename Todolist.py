#Todolist

num = int(input("choose a mode by entering a number \
                 1.Add a task \
                 2.View list \
                 3.Exit"))
                 
task =["Buy clothes", "Pay Bills", "Ring parents"]

if num == 1:
    new_task =input("Enter task")
    task.append(new_task)
    print(task)    

if num == 2:
    print(task)
    
if num == 3:
    print("quit")

    

