# Documentation

- [Main Title](#Main-Title)
- [Data Nodes](#DataNodes)
- [Creating Files](#CreatingFiles)


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
