   # AirBnB clone - The console


![The console](https://github.com/Leidysalda/prueba/blob/master/FirstStep.png?raw=true)


# First step: Write a command interpreter to manage your AirBnB objects.


This is the first step towards creating the first complete web app - the AirBnB clone.

Each task is linked:

A main class (called BaseModel) is established to handle initialization, serialization and deserialization of future instances, a simple serialization / deserialization flow will be created: Instance <-> Dictionary <-> JSON string <-> file, will be created all classes used for AirBnB (User, State, City, Place ...) that inherit from BaseModel, the first abstracted storage engine of the project will be created: file storage.


All unit tests will be created to validate all our classes and storage engine.


# Starting 🚀

[![The console](http://img.youtube.com/vi/p00ES-5K4C8/0.jpg)](http://www.youtube.com/watch?v=p00ES-5K4C8 "AirBnB The Console")



# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to create a Python package

How to create a command interpreter in Python using the cmd module

What is Unit testing and how to implement it in a large project

How to serialize and deserialize a Class

How to write and read a JSON file

How to manage datetime

What is an UUID

What is *args and how to use it

What is **kwargs and how to use it

How to handle named arguments in a function


# Execution

Your shell should work like this in interactive mode:

``` python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```

# Execute program called _console.py_

Cotains:

- prompt:       (hbnb)
- quit:	        exit the program
- help:         keep it updated
- create:       creates a new instance of BaseModel
- show:         prints the string representation of an instance based on the class name and id
- destroy:      deletes an instance based on the class name and id
- all:          prints all string representation of all instances based or not on the class name
- update:       updates an instance based on the class name and id by adding or updating attribute 


``` python

guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907',
'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9',
'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717),'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}",
"[BaseModel] (49faff9a-6318-451f-87b6-910505c55907){'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907',
'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)

```

# Running the tests ⚙️


They will be tested file by file using this command: python3 -m unittest tests / test_models / test_base_model.py


```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$

```

# Deployment 📦

### Final Product
![Project](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png)


# Authors ✒️


* **Leidy J. Saldaña** - *AirBnB Clone - The Console* - [Leidysalda](https://github.com/leidysalda)
* **Juan Carlos Rengifo** - *AirBnB Clone - The Console* - [juankarlos999](https://github.com/juankarlos999)


---
Thank you fo reading 😊
