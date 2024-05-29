# File: lib/TodoList.py
from lib.Todo import Todo

# Design a multi class program - https://journey.makers.tech/pages/design-a-multi-class-program-python

class TodoList:
    def __init__(self):
        self.myList = []

    def add(self, Todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.myList.append(Todo)

    def list_incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete

        # todo
        # filtered_list = [t for t in self.myList if t.isComplete()]
        # return filtered_list

        return [
            Todo for Todo in self.myList
            if not Todo.complete
        ]

        return self.myList

    def list_complete(self):
        # Todo - check state
        return [
            Todo for Todo in self.myList
            if  Todo.complete
        ]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

