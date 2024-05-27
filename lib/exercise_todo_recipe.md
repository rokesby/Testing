# {{PROBLEM}} Todo Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE


def retrieve_task_list():
    
    Parameters: 
        none

    Returns: (a list of strings/tasks that are not complete)
        a list of strings
        an empty list of no active tasks exist


    Side effects: 
        none
    """
    
```

def mark_complete(task_description):
    
    Parameters: 
        task_description : The name of a task which should disappear from the task list

    Returns:
        none

    Side effects: 
        Do not do anything, or maybe raise an exception if the specified task does not exist
    """
    pass # Test-driving means _not_ writing any code here yet.
```


def add_todo(task_description):
    """
    Parameters:
        task_description : a short description of the task at hand e.g. buy some milk.

    Returns: 
        none

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Retrieve the todolist when no tasks have been added
It returns an empty list

"""
retrieve_empty_todo_list() => []

"""
Add 1 task and then retrieve the list
Returns a list of 1 element

"""
retrieve_populated_list("my task") => ["my task"]

"""
Add 2 tasks and then retrieve the list
Returns a list of 2 elements


"""

retrieve_populated_list2("my task", "second task") => ["my task","second task"]
"""
Remove a todo when it doesn't exist e.g. empty list
Raise an exception to state the error

"""

remove_from_empty_list ("Task description") => Exception

"""
Remove a todo right after adding one.
Returns an empty list with no error


"""

remove_from_populated_list ("Task description") => []

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
