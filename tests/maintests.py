import sys
import os

module_folder = r"src\datarack"
sys.path.append(os.path.abspath(module_folder))

from datarack import *

print("File Created")
create_file("test.txt")

print("Define DataNode")
test = DataNode(["TEST1", "TEST2", "TEST3"])

print("Testing DataNode Adding Functionality")
add_node(test, "1", ["1.1", "1.2", "1.3"], "test.txt")
add_node(test, "2", ["2.1", "2.2", "2.3"], "test.txt")
add_node(test, "3", ["3.1", "3.2", "3.3"], "test.txt")
insert_node(test, 2, "4", ["4.1", "4.2", "4.3"], "test.txt")

text_to_csv(test, "test.csv", "test.txt")

# More testing will be done in the future