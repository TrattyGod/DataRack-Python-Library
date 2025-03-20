import os
import csv
import sys



class DataNode:
    """
    DataNode class stores the categories of the data

    Parameters:
    categories (list) - all the categories of the data
    """
    def __init__(self, categories):
        self.categories = categories



    """
    Displays all categories, and ID, with their respective indexes
    """
    def display_data(self):
        print("IDX: 0 | ID")
        self.idx = 1
        for category in self.categories:
            print(f"IDX: {self.idx} | {category}")
            self.idx += 1



def create_file(name, location=None):
    """
    Creates a new file, or clears an already existing one. If no location is given, it will use the directory location. The file will be a text file with the header: <<DataRack File>>

    Parameters:
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    with open(file_path, "w") as file:
        file.write("<< DataRack File, Do Not Manually Edit >>")

    with open(file_path, "a") as file:
        file.write("\n")
        file.write("\n")
         


def clear_file(name, location=None):
    """
    Creates a new file, or clears an already existing one. If no location is given, it will use the directory location. The file will be a text file with the header: <<DataRack File>>

    Parameters:
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    with open(file_path, "w") as file:
        file.write("<< DataRack File, Do Not Manually Edit >>")

    with open(file_path, "a") as file:
        file.write("\n")
        file.write("\n")



def get_idx_from_id(datanode, ID, name, location=None):
    """
    Gets the index of a DataNode from its ID. (will only find the first DataNode with the matching ID)

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    ID (string) - An ID for the node that can be used to easily retrieve its data
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    The index as an integer
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    all_nodes = read_all(datanode, file_path)
    idx = 0
    for node in all_nodes:
        if (node[0] == ID):
            break
        
        idx += 1

    return idx



def get_all_idx_from_id(datanode, ID, name, location=None):
    """
    Gets the index of a DataNode from its ID. (will find all DataNodes with the matching ID)

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    ID (string) - An ID for the node that can be used to easily retrieve its data
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    A list of the index as integers
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    all_nodes = read_all(datanode, file_path)
    all_idx = []
    idx = 0
    for node in all_nodes:
        if (node[0] == ID):
            all_idx.append(idx)
        
        idx += 1
        
    return all_idx



def add_node(datanode, ID, values, name, location=None):
    """
    Adds a DataNode with an ID, and data for all the categories to text file. The text file MUST have been made with this module.

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    ID (string) - An ID for the node that can be used to easily retrieve its data
    values (list) - The corresponding values for all the categories for the DataNode (cannot have more or less items than amount of categories in DataNode)
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    idx = 0
    with open(file_path, "a") as file:
        file.write(f"ID: {ID}")
        file.write("\n")
        for item in datanode.categories:
            file.write(f"{item.upper()}: {values[idx]}")
            file.write("\n")
            idx += 1
       
        file.write("\n")



def insert_node(datanode, index, ID, values, name, location=None):
    """
    Inserts a DataNode by index. Doesn't remove or edit existing nodes

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    index (int) - the index where the new node gets inserted
    ID (string) - An ID for the node that can be used to easily retrieve its data
    values (list) - The corresponding values for all the categories for the DataNode (cannot have more or less items than amount of categories in DataNode)
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    with open(file_path, "r") as file:
        lines = file.readlines()

    lineNum = 2 + (index * (len(datanode.categories) + 2))

    i = 0
    lines.insert(lineNum + i, f"ID: {ID}")
    i += 1
    lines.insert(lineNum + i, "\n")
    i += 1
    idx = 0
    for item in datanode.categories:
        lines.insert(lineNum + i, f"{item.upper()}: {values[idx]}")
        i += 1
        lines.insert(lineNum + i, "\n")

        idx += 1
        i += 1

    lines.insert(lineNum + i, "\n")

    idx = 0
    with open(file_path, "w") as file:
        file.writelines(lines)



def remove_node(datanode, idx, name, location=None):
    """
    Removes a node from a DataRack file using its index 

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    idx (int) - the index of the node in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    lineNum = 3 + (idx * (len(datanode.categories) + 2))
    linesToRemove = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        linesToRemove.append(lineNum)
       
        i = 0
        for line in range(len(datanode.categories)):
            linesToRemove.append(lineNum + i - 1)

            i += 1

        updatedLines = [line for i, line in enumerate(lines) if i not in linesToRemove]
        updatedLines.pop(lineNum - 1)
        updatedLines.pop(lineNum - 1)
        updatedLines = ''.join(updatedLines)

        file.write(updatedLines)



def replace_node(datanode, index, ID, values, name, location=None):
    """
    Replaces a DataNode by index. All values will be overwritten.

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    index (int) - the index of the node that needs to be replaced
    ID (string) - An ID for the node that can be used to easily retrieve its data
    values (list) - The corresponding values for all the categories for the DataNode (cannot have more or less items then amount of categories in DataNode)
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    remove_node(datanode, index, file_path)
    insert_node(datanode, index, ID, values, file_path)



def replace_by_id(datanode, ID, newID, values, name, location=None):
    """
    Replaces a DataNode by ID. It will only replace the first one it finds.

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    ID (string) - The ID of the node that needs to be replaced
    newID (string) - An ID for the node that can be used to easily retrieve its data
    values (list) - The corresponding values for all the categories for the DataNode (cannot have more or less items then amount of categories in DataNode)
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)
    
    idx = get_idx_from_id(datanode, ID, file_path)
    replace_node(datanode, idx, newID, values, file_path)



def replace_all_by_id(datanode, ID, newID, values, name, location=None):
    """
    Replaces a DataNode by ID. It will replace all the ones it finds, and give all of them the same new values.

    Parameters:
    datanode (DataNode) - the DataNode object you want to add to the file
    ID (string) - The ID of the node that needs to be replaced
    newID (string) - An ID for the node that can be used to easily retrieve its data
    values (list) - The corresponding values for all the categories for the DataNode (cannot have more or less items then amount of categories in DataNode)
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)
    
    idx = get_all_idx_from_id(datanode, ID, file_path)

    for index in idx:
        replace_node(datanode, index, newID, values, file_path)



def read_node(datanode, idx, name, location=None):
    """
    Reads the values of a node using its index. 

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    idx (int) - the index of the node in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    A list containing the values of the DataNode, and its ID (index 0)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    lineNum = 3 + (idx * (len(datanode.categories) + 2))
    data = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    i = 0
    for line in range(len(datanode.categories) + 1):
        addedData = lines[lineNum + i - 1].rstrip("\n")
        addedData = addedData.split(":", 1)[1]

        data.append(addedData.lstrip())
        i += 1

    return data
   


def read_by_id(datanode, ID, name, location=None):
    """
    Returns the values of the first node in a file with the given ID.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the node in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    A list containing the values of the DataNode, and its ID (index 0)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)
   
    data = []
   
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    index = get_idx_from_id(datanode, ID, file_path)
    data = read_node(datanode, index, file_path)
                   
    return data



def read_all_by_id(datanode, ID, name, location=None):
    """
    Returns a nested list of the values of all nodes in a file with the given ID.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the nodes in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    A nested list containing the values of the DataNodes, and their IDs (index 0)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)
   
    all_data = []

    index = get_all_idx_from_id(datanode, ID, file_path)
    for idx in index:
        all_data.append(read_node(datanode, idx, file_path))
                   
    return all_data



def remove_by_id(datanode, ID, name, location=None):
    """
    Removes the first DataNode in file with the given ID.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the node in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    index = get_idx_from_id(datanode, ID, file_path)
    remove_node(datanode, index, file_path)



def remove_all_by_id(datanode, ID, name, location=None):
    """
    Removes all DataNodes in file with the given ID.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the nodes in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)
    
    while True:
        remove_by_id(datanode, ID, name, location)

        with open(file_path, "r") as file:
            lines = file.readlines()

        foundMore = False
        for line in lines:
            if (line.lstrip().rstrip() == "ID: " + ID):
                foundMore = True

        if (foundMore == False):
            break



def read_all(datanode, name, location=None):
    """
    Returns the value of all DataNodes in a file in a nested list.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the node in the file
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    A nested list containing the values and IDs (index 0) of every DataNode
    """
    if location != None:
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    all_data = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    while lines and lines[-1].strip() == '':
        lines.pop()

    idx = 0
    while 3 + idx * (len(datanode.categories) + 2) < len(lines):
        data = read_node(datanode, idx, name, location)
        all_data.append(data)
        idx += 1

    return all_data



def find_node(datanode, ID, values, findAll, name, location=None):
    """
    Filters nodes and returns a list/nested list of all nodes with the given requirements.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    ID (string) - the ID of the nodes in the file (set to # to ignore)
    values (list) - the values of the nodes in the file (set any categories to # to ignore them)
    findAll (bool) - If true, will return a nested list of all datanodes. If false, will return a single list with the values of the datanode.
    name (string) - the file name (.txt)
    location (string) - the file path (OPTIONAL)

    Returns:
    findAll = True: A nested list containing the values and IDs (index 0) of every DataNode with the given requirements
    findAll = False: A list containing the values and ID (index 0) of the DataNode with the given requirements
    """
    if (location != None):
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    if (ID == "#"):
        all_nodes = read_all(datanode, file_path)
    else:
        all_nodes = read_all_by_id(datanode, ID, file_path)

    foundNodes = []
    matchingValues = 0

    for node in all_nodes:
        matchingValues = 0
        i = 0
        for value in values:
            if (value == "#"):
                matchingValues += 1
            else:
                if (value == node[i + 1]):
                    matchingValues += 1

            i += 1

        if (matchingValues == len(node[1:])):
            foundNodes.append(node)

    if (findAll):
        return foundNodes
    else:
        return foundNodes[0]



def csv_to_node(name, location=None):
    """
    Creates a DataNode object using a CSV file. The DataNode will have categories equivelent to the CSV file column names

    Parameters:
    name (string) - the file name (.csv)
    location (string) - the file path (OPTIONAL)

    Returns:
    DataNode object with categories set to CSV column names
    """
    if location != None:
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    with open(file_path, 'r') as file:
        reader = csv.reader(file)  
        data = list(reader)      

    columns = list(zip(*data))
    columns = [list(column)[0] for column in columns]

    datanode = DataNode(columns)

    return datanode



def csv_to_text(datanode, ID, csv_name, name, csv_location=None, location=None):
    """
    Uses DataNode object to fill a DataRack file with the contents of a csv file. All IDs will be set to one value.  

    Parameters:
    datanode (DataNode) - the DataNode object of the file - *Use the DataNode object created with csv_to_node()*
    ID (string) - the ID that all DataNodes in the text file will be set to
    csv_name (string) - the file name of the CSV file (.csv)
    name (string) - the file name of the text file (.txt)
    csv_location (string) - the file path of the csv file (OPTIONAL)
    location (string) - the file path of the text file (OPTIONAL)
    """
    if location != None:
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    if csv_location != None:
        csv_file_path = os.path.join(csv_location, csv_name)
    else:
        csv_file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), csv_name)

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader]

        clear_file(name, location)
        
        for row in rows:
            data = []
            for item in row:
                data.append(item)
            
            add_node(datanode, ID, data, name, location)



def text_to_csv(datanode, csv_name, name, csv_location=None, location=None):
    """
    Uses DataNode object to fill a csv file with the contents of a DataRack text file.

    Parameters:
    datanode (DataNode) - the DataNode object of the file
    csv_name (string) - the file name of the CSV file (.csv)
    name (string) - the file name of the text file (.txt)
    csv_location (string) - the file path of the csv file (OPTIONAL)
    location (string) - the file path of the text file (OPTIONAL)
    """
    if location != None:
        file_path = os.path.join(location, name)
    else:
        file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), name)

    if csv_location != None:
        csv_file_path = os.path.join(csv_location, csv_name)
    else:
        csv_file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), csv_name)

    data = []
    first_row = datanode.categories
    print(first_row)
    
    data.append(first_row)
    rows = read_all(datanode, name, location)

    for row in rows:
        for item in row:
            row = [item.lstrip() for item in row]
        data.append(row)
    
    data[0].insert(0, "ID")

    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
