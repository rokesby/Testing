from lib.TodoList import TodoList

# Should be an empty list as nothing has been added to it.
def test_initially_complete_is_empty():
    myTodolist = TodoList()
    result = myTodolist.list_complete()
    assert result == []