Welcome to the AirBnB Clone Project! The aim of this project is to build a functional replica of the popular Airbnb platform, starting with the implementation of a command interpreter. This foundational step is crucial as it lays the groundwork for subsequent development phases, including HTML/CSS templating, database storage, API integration, and front-end incorporation.

At the core of the project is the creation of a command interpreter, akin to a simplified shell. This command interpreter facilitates the management of AirBnB objects, allowing users to perform various actions such as creating, retrieving, updating, and deleting objects. The interpreter employs a serialization and deserialization flow that encompasses the conversion of instances into dictionaries, JSON strings, and files.

Starting and Using the Command Interpreter:

To initiate the AirBnB command interpreter, follow these steps:

Open a terminal.
Navigate to the project's root directory.
Run the console.py script using the command: ./console.py
Once the interpreter is active, you'll be greeted with a prompt (hbnb), indicating that you are in the command interpreter environment. You can now interact with the interpreter by entering various commands to manage AirBnB objects.

Examples of Usage:

Creating an object:

sql
(hbnb) create User
Retrieving an object:

sql
(hbnb) show User 1234-5678-1234
Listing all objects:

scss
(hbnb) all
Updating an object's attribute:

sql
(hbnb) update User 1234-5678-1234 first_name "John"
Deleting an object:

scss
(hbnb) destroy User 1234-5678-1234
Exiting the interpreter:

scss
(hbnb) quit
