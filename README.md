AirBnb_clone
This is a clone of an AirBnb according to the SDLC and my understanding of the project I am only supposed to implement which is the bulding of the software, perform testing and integration if needed.
This is the first part which is the Console which will act as my frontend.

# AirBnB Clone Command Interpreter

This command interpreter is the first step towards building an AirBnB clone. It serves as the backbone for managing AirBnB objects through a command-line interface.

## Overview

The objective of this project is to develop a command-line interface to manage various objects within the AirBnB clone. This includes functionalities such as creating new objects, retrieving objects from storage, performing operations on objects, updating object attributes, and destroying objects.

## Project Structure
The project involves several key tasks that form the foundation of the AirBnB clone:

1. **BaseModel Class**: Implementation of a parent class called `BaseModel` responsible for initialization, serialization, and deserialization of future instances.
2. **Serialization/Deserialization Flow**: Creation of a simple flow for serialization/deserialization, involving instances, dictionaries, JSON strings, and file storage.
3. **Class Definitions**: Creation of all necessary classes for AirBnB objects such as `User`, `State`, `City`, `Place`, etc., all of which inherit from the `BaseModel` class.
4. **Storage Engine**: Development of the first abstracted storage engine for the project, specifically focusing on file storage.
5. **Unit Tests**: Writing comprehensive unit tests to validate the functionality of all classes and storage engines.

## Command Interpreter

The command interpreter is designed to handle various operations on AirBnB objects, including:

- Creating new objects (e.g., users, places)
- Retrieving objects from storage (e.g., file, database)
- Performing operations on objects (e.g., counting, computing statistics)
- Updating attributes of objects
- Destroying objects

Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
