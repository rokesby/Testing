# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

Allow the user to manage a list of tasks/todos to improve productivity

- Tasks are DONE (boolean)

- Managing a list of tasks - 
- Create a list, add tasks to it
- Return a list of complete or incomplete tasks
- Declare task bankruptcy and mark them as all complete.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```See image diagram in Logseq
```

_Also design the interface of each class in more detail._

```python
class TodoList
..... blah


class Todo:
    .... blah
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Create a new todolist and add two new incomplete tasks to it
We see two tasks in the resulting incomplete list and nothing in the complete list

We create two tasks, mark one as complete, then retrieve two lists (complete/incomplete), each with one entry each

As above, but we 'give up' and find that nothing incomplete is returned
"""


```


## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
"""

TodoList
- We ask for a list of tasks when the list is empty


Todo (nothing returned so really hard to test.)
- We create a task - observe no errors
- We create a task, complete it - observe no errors 

"""
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
