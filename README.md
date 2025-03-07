# Documentation

- [Installing and Importing](#Installing-and-Importing)
- [Data Nodes](##Data-Nodes)
- [Creating Files](##Creating-Files)
- [Adding DataNodes](##Adding-DataNodes)
- [Deleting DataNodes](##Deleting-DataNodes)
- [Replacing DataNodes](##Replacing-DataNodes)
- [Reading DataNodes](##Reading-DataNodes)
- [Filtering](##Filtering)
- [Other](##Other)
- [CSV Tools](##CSVTools)


## Installing and Importing

Luckily, installing DataRack is extremely simple

```bash
pip install datarack
```

To import it into your python project, use:
```python
from DataRack import *
```

## DataNodes

DataNodes are a type of data, taylored towards your project. They each have their own set of "categories":

```python
# Creates a DataNode with categories "Name" and Age
my_datanode = DataNode(["Name", "Age"])
```

If you ever need to see the categories:
```python
# Prints out the categories and ID
my_datanode.display_data()
```


## Creating Files

Creating files in DataRack is extremely simple

```python
# Creates a file named "DataFile"
create_file("DataFile.txt")
```

create_file() takes 2 parameters:
1. File name (String)
2. File location (String) *Optional, if not specified will be set to the project directory*

clear_file() does the same thing. 

```python
# Clears the file, and creates it if it doesn't find it
clear_file("DataFile.txt")
```

Both functions will auto-create a file if they don't find one. Additionally, files created using the module will have a <<DataRack File, Do Not Manually Edit>> header. Files used by this module must have this header, and shouldn't be manually edited.

## Adding DataNodes

DataNodes can be added to a file using a few different methods. To push one to a file, you can use the add_node() function

```python
# Creates a DataNode
person = DataNode(["Name", "Age", "Gender"])

create_file("PEOPLE.txt")

add_node(person, "Default", ["Bob", "57", "Male"], "test.txt")
add_node(person, "Default", ["Marie", "25", "Female"], "test.txt")
```

The file will look like this:

```text
<<DataRack File, Do Not Manually Edit>>

ID: Default
NAME: Bob
AGE: 57
GENDER: Male

ID: Default
NAME: Marie
AGE: 25
GENDER: Female
```

add_node() takes 5 parameters:
1. datanode (DataNode)
2. ID (String) - A "tag" associated with the data that makes it easier to access
3. values (List) - All of the data for each category, must be same length as datanode.categories
5. File name (String)
6. File location (String) *Optional, if not specified will be set to the project directory*

**Similarly, insert_node() allows you to insert a chunk of data somewhere in a file, using an index**

insert_node() takes 6 parameters:
1. datanode (DataNode)
2. index (Int) - The index, each DataNode gets an index based on where it is located 
3. ID (String) - A "tag" associated with the data that makes it easier to access
4. values (List) - All of the data for each category, must be same length as datanode.categories
5. File name (String)
6. File location (String) *Optional, if not specified will be set to the project directory*

```python
# Creates a DataNode
person = DataNode(["Name", "Age", "Gender"])

create_file("PEOPLE.txt")

add_node(person, "Default", ["Bob", "57", "Male"], "test.txt")
add_node(person, "Default", ["Marie", "25", "Female"], "test.txt")

# inserts node in between "Bob" and "Marie"
insert_node(person, 1, "Default", ["Mark", 15, "Male"], "test.txt")
```

## Deleting DataNodes

DataRack supports many ways of removing DataNodes from a text file:

```python
# Creates a DataNode
person = DataNode(["Name", "Age", "Gender"])

create_file("PEOPLE.txt")

add_node(person, "Default", ["Bob", "57", "Male"], "test.txt")
add_node(person, "Default", ["Marie", "25", "Female"], "test.txt")

# removes DataNode with index 1 (second chunk of data in the file)
remove_node(person, 1, "test.txt")
```

remove_node() takes 4 parameters:
1. datanode (DataNode)
2. index (Int) - The index, each DataNode gets an index based on where it is located 
3. File name (String)
4. File location (String) *Optional, if not specified will be set to the project directory*

**Alternataly, you can remove nodes by their ID**

remove_by_id() takes 4 parameters:
1. datanode (DataNode)
2. ID (String) - The ID of the DataNodes you want to remove
3. File name (String)
4. File location (String) *Optional, if not specified will be set to the project directory*

remove_by_id() will only remove the first DataNode it finds. To remove all DataNodes with the specified ID, use remove_all_by_id() *Same Parameters*

## Replacing DataNodes

If you want to replace a node, you can do so in multiple different ways:

```python
# Creates a DataNode
person = DataNode(["Name", "Age", "Gender"])

create_file("PEOPLE.txt")

add_node(person, "Default", ["Bob", "57", "Male"], "test.txt")
add_node(person, "Default", ["Marie", "25", "Female"], "test.txt")

# replaces DataNode with index 1
replace_node(person, 1, "New ID", ["New name", "New age", "New gender"], "test.txt")
```

replace_node() takes 6 parameters:
1. datanode (DataNode)
2. index (Int) - The index, each DataNode gets an index based on where it is located
3. ID (String) - The new ID
4. values (List) - The new values
5. File name (String)
6. File location (String) *Optional, if not specified will be set to the project directory*

**Alternataly, you can replace nodes by their ID**

replace_by_id() takes 7 parameters:
1. datanode (DataNode)
2. index (Int) - The index, each DataNode gets an index based on where it is located
3. ID (String) - The ID of the DataNode you want to replace
4. newID (String) - The new ID
5. values (List) - The new values
6. File name (String)
7. File location (String) *Optional, if not specified will be set to the project directory*

replace_by_id() will only replace the first DataNode it finds. To replace all DataNodes with the specified ID, use replace_all_by_id() *Same Parameters*
