AirBnB Clone Project

Description
The AirBnB Clone project replicates key functionalities of the AirBnB platform. 

Command Interpreter
A shell-like tool for managing AirBnB objects. 
It allows for creating, updating, deleting, and retrieving instances.

How to Start
Clone the Repository:
git clone https://github.com/yourusername/AirBnB_clone.git
cd AirBnB_clone

Run the Interpreter:
./console.py

Commands
create <ClassName>: Create a new instance.
show <ClassName> <id>: Display an instance.
destroy <ClassName> <id>: Delete an instance.
all [ClassName]: List all instances, or instances of a specific class.
update <ClassName> <id> <attr> "<value>": Update an attribute.
quit: Exit the interpreter.

Examples
Create a User:

(hbnb) create User
e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c

Show a User:

(hbnb) show User e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c
[User] (e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c) {'id': 'e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c', 'created_at': '2024-08-07T12:34:56.789012', 'updated_at': '2024-08-07T12:34:56.789012'}

Update a User:

(hbnb) update User e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c name "John Doe"

List Users:


(hbnb) all User
[[User] (e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c) {'id': 'e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c', 'created_at': '2024-08-07T12:34:56.789012', 'updated_at': '2024-08-07T12:34:56.789012', 'name': 'John Doe'}]

Delete a User:

(hbnb) destroy User e3b625fc-f7e4-4c19-9f37-b9d9f5268c7c
