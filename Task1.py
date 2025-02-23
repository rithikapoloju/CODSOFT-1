def menu():
     print("TO DO LIST MENU:")
     print("1:to add task")
     print("2:to display tasks & status")
     print("3:to mark task as done")
     print("4:to delete task")
     print("5:TO Exit")
     
tasks=[]
status=[]

while True:
    
    menu()
    choice=input("enter your choice:")
    if choice=="1":
        task = input("enter task: ")
        tasks.append(task)
        status.append(False)
        print("task added successfully\n")
    elif choice=="2":
        if not tasks:
            print("no tasks found to mark as done\n")
        else:
            print("\n")
            print("To Do List\n")
            i=0
            while i < len(tasks):
                taskstatus="✔ DONE" if status[i]  else "❌ NOT DONE"
                print(f"{i+1}. {tasks[i]}[{taskstatus}]\n")
                i+=1
    elif choice=="3":
             if not tasks:
                  print("no tasks found")
             else:
                 num=int(input("enter task number to mark as done: \n"))
                 if 1<=num<=len(tasks):
                     status[num-1]=True
                     print("Task marked as done\n")
                 else:
                     print("invalid task number")

    elif choice=="4":
          if not tasks:
            print("no tasks found to be deleted\n")
          else:
               num=int(input("enter task number to delete: \n"))
               if 1<=num<=len(tasks):
                  del tasks[num-1]
                  del status[num-1]
                  print("task deleted successfully\n")
               else:
                    print("invalid task number")
    elif choice=="5":
        print("Exited\n")
        break
        
     
          
               
               
  

