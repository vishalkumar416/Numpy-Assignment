# Q1. Difference in Data Types Between list_ and array_list
import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

# Printing data types
print("Data type of list_:", type(list_))
print("Data type of array_list:", type(array_list))

# Q2. Data Type of Each Element in list_ and array_list
# Data type of each element in list_
print("Data types of elements in list_:")
for elem in list_:
    print(type(elem))

# Data type of each element in array_list
print("Data types of elements in array_list:")
for elem in array_list:
    print(type(elem))

# Q3. Effect of Changing dtype in array_list
array_list = np.array(object=list_, dtype=int)

# Data type of each element in list_ and array_list
print("Data types of elements in list_:")
for elem in list_:
    print(type(elem))

print("Data types of elements in array_list:")
for elem in array_list:
    print(type(elem))

# Q4. Characteristics of num_array
num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)

# Shape of num_array
print("Shape of num_array:", num_array.shape)

# Size of num_array
print("Size of num_array:", num_array.size)

# Q5. Create a 3×3 Matrix of Zeros
zero_matrix = np.zeros((3, 3))
print("3x3 Zero Matrix:")
print(zero_matrix)

# Q6. Create a 5×5 Matrix of Zeros
identity_matrix = np.eye(5)
print("5x5 Identity Matrix:")
print(identity_matrix)
