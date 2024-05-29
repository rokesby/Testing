class TodoSimple:

    def __init__(self):
        self.todo_list = []


    def get_list(self):
        return self.todo_list
    
    def add_task(self, task_description):
        self.todo_list.append(task_description)
        return self.todo_list

    def mark_complete(self, task_description):
        # self.todo_list.append(task_description)
        if task_description in self.todo_list:
            # Remove the item and then return the list.
            self.todo_list.remove(task_description)
            return self.todo_list
        else:
            raise Exception("Task does not exist")
        