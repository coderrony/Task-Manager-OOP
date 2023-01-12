from uuid import uuid4
import time
import datetime


class Task:

    __all_task = []  # all_task is a private list which store Task object as a dictionary

    task_count = 1  # task_count increase by 1 for each object creation

    def __init__(self, name=None) -> None:
        self.ID = str(uuid4())
        self.taskNUM = self.task_count
        self.name = name
        self.createTime = str(time.strftime("%m/%d/%y")) + " " + \
            str(datetime.datetime.now().strftime('%H:%M:%S'))
        self.updateTime = "NA"
        self.completeTask = False
        self.completeTime = "NA"

        if name != None:  # without name the task not add the __all_task list
            self.__all_task.append(vars(self))
            print("\nTask Create Successfully\n")
            Task.task_count += 1

    # this __print_item is a private method which not call outside the class
    def __print_item(self, item, taskNo=True):
        if taskNo:
            print("")
        print(f"ID - {item['ID']}")
        print(f"Task - {item['name']}")
        print(f"Create time - {item['createTime']}")
        print(f"Update time - {item['updateTime']}")
        print(f"Completed - {item['completeTask']}")
        print(f"Completed time - {item['completeTime']}")
        print("")

    def show_task(self):
        if len(self.__all_task) == 0:
            print("\nNo Task Available\n")
        else:
            for item in self.__all_task:
                self.__print_item(item)

    def show_incomplete(self):
        isFound = False
        for item in self.__all_task:
            if item['completeTask'] == False:
                isFound = True
                self.__print_item(item)
        if not isFound:
            print("\nNo Incomplete Task\n")

    def show_complete(self):
        isFound = False
        for item in self.__all_task:
            if item['completeTask'] == True:
                isFound = True
                self.__print_item(item)
        if not isFound:
            print("\nNo Complete Task\n")

    def update_task(self):

        taskFound = False
        if len(self.__all_task) == 0:
            print("\nNo Task Available\n")
        else:
            for item in self.__all_task:
                if item['completeTask'] == False:
                    taskFound = True
                    print(f"\nTask No - {item['taskNUM']}")
                    self.__print_item(item, False)
            if taskFound:
                choice = int(input("Enter Task No: "))
                newTaskName = input("Enter New Task: ")
                for chk in self.__all_task:
                    if chk['taskNUM'] == choice:

                        chk['name'] = newTaskName
                        chk['updateTime'] = str(time.strftime("%m/%d/%y")) + " " + \
                            str(datetime.datetime.now().strftime('%H:%M:%S'))

                        print("\nTask Update Successfully\n")
                        break
            else:
                print("\n No Task To Update\n")

    def complete_task(self):

        taskFound = False
        if len(self.__all_task) == 0:
            print("\nNo Task Available\n")
        else:
            for item in self.__all_task:
                if item['completeTask'] == False:
                    taskFound = True
                    print(f"\nTask No - {item['taskNUM']}")
                    self.__print_item(item, False)
            if taskFound:
                choice = int(input("Enter Task No: "))
                for chk in self.__all_task:
                    if chk['taskNUM'] == choice:
                        chk['completeTime'] = str(time.strftime("%m/%d/%y")) + " " + \
                            str(datetime.datetime.now().strftime('%H:%M:%S'))
                        chk['completeTask'] = True

                        print("\nTask Complete Successfully\n")
                        break
            else:
                print("\n All Task is Completed\n")

    def __repr__(self) -> str:  # decorators method from python
        print(f"id: {self.ID} name: {self.name}")


system = Task()  # this task create default it's not add
while True:
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show completed Tasks")
    print("5. Update Tasks")
    print("6. Mark A Task Completed")
    choice = int(input("Enter Option: "))

    if choice == 1:
        name = input("Enter New Task: ")
        Task(name)
    elif choice == 2:
        system.show_task()
    elif choice == 3:
        system.show_incomplete()
    elif choice == 4:
        system.show_complete()
    elif choice == 5:
        system.update_task()
    elif choice == 6:
        system.complete_task()
    else:
        break
