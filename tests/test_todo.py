from lib.todo import Todo
import pytest


def test_retrieve_empty_list():
    myTodo = Todo()
    assert myTodo.get_list() == []


def test_populated_list():
    myTodo = Todo()
    myTodo.add_task("My first task")
    assert myTodo.get_list() == ['My first task']


def test_populated_list2():
    myTodo = Todo()
    myTodo.add_task("My first task")
    myTodo.add_task("My second task")
    assert myTodo.get_list() == ['My first task', 'My second task']

def test_remove_from_list():
    myTodo = Todo()
    myTodo.add_task("My first task")
    myTodo.mark_complete("My first task")
    assert myTodo.get_list() == []


def test_remove_from_list_bad():
    myTodo = Todo()
    myTodo.add_task("My first task")
    
    with pytest.raises(Exception) as e:
        myTodo.mark_complete("My first task 2222")
    error_message = str(e.value)
    assert error_message == "Task does not exist"

# def test_remove_empty():
#     myTodo = Todo()
#     myTodo.add_task("My first task")
#     myTodo.add_task("My second task")
#     assert myTodo.get_list() == ['My first task', 'My second task']