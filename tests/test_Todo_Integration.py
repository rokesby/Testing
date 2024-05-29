from lib.TodoList import TodoList
from lib.Todo import Todo

# Should be an empty list as nothing has been added to it.
def test_create_todolist():
    myTodolist = TodoList()
    result = myTodolist.list_complete()
    assert result == []


# Add an element to the list and confirm an incomplete list of 1 is returned.
def test_add_one_element():
    myTodo = Todo('Make breakfast')
    myTodoList  = TodoList()
    myTodoList.add(myTodo)
    result = myTodoList.list_incomplete()
    assert result == [myTodo]

    # Todo - check the property state later on. both complete and incomplete.

def test_two_elements():
    
    myTodoList  = TodoList()

    myTodo = Todo('Make breakfast')
    myTodoList.add(myTodo)

    myTodo2 = Todo('5km run')
    myTodoList.add(myTodo2)
 
    result = myTodoList.list_incomplete()
    assert result == [myTodo, myTodo2]

def test_marks_one_of_two_as_complete():
    myTodoList  = TodoList()

    myTodo = Todo('Make breakfast')
    myTodoList.add(myTodo)

    myTodo2 = Todo('5km run')
    myTodoList.add(myTodo2)

    myTodo2.mark_complete()

    result = myTodoList.list_incomplete()
    assert result == [myTodo]


def test_marks_tasks_as_complete_and_adds_to_complete_list():
    
    myTodoList  = TodoList()

    myTodo = Todo('Make breakfast')
    myTodoList.add(myTodo)

    myTodo2 = Todo('5km run')
    myTodoList.add(myTodo2)

    myTodo2.mark_complete()    

    assert myTodoList.list_complete() == [myTodo2]

"""

┌─────────────────────┐      
│                     │      
│                     │      
│     TaskList        │      
│                     │      
│     - complete      │      
│                     │      
│                     │      
│                     │      
└──────────┬──────────┘      
           │                 
           │                 
           │                 
           │                 
           │                 
 ┌─────────▼───────────┐     
 │                     │    ▼
 │  Todo               │     
 │                     │     
 │ - incomplete        │     
 │                     │     
 │                     │     
 │                     │     
 │                     │     
 └─────────────────────┘     

"""