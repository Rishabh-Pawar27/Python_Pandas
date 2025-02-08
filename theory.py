# What is NumPy?
'''
NumPy (Numerical Python) is a powerful Python library used for scientific computing, data analysis, and numerical operations. It provides multi-dimensional arrays and mathematical functions optimized for performance.
'''

# Why Use NumPy?
'''
=> Fast & Efficient: Much faster than Python lists.
=> Multi-Dimensional Arrays: Supports 1D, 2D, and 3D arrays.
=> Mathematical Operations: Performs vectorized operations (addition, multiplication, etc.).
=> Statistical & Linear Algebra: Includes functions for mean, standard deviation, matrix operations.
=> Integration with Pandas, Matplotlib, and ML Libraries (Scikit-Learn, TensorFlow).
'''

# Why Use NumPy for Data Analysis?
'''
NumPy is the foundation of data analysis in Python because it provides fast, efficient, and powerful tools for handling large datasets. Here's why data analysts prefer NumPy over Python lists:

1. Faster Computation (Performance Boost):-
=> NumPy arrays are 50x faster than Python lists because they use C & Fortran under the hood.
=> Supports vectorized operations, meaning you can apply functions to entire arrays instead of looping.

2. Multi-Dimensional Data Handling:-
=> NumPy supports 1D (Vectors), 2D (Tables), and 3D+ (Multidimensional) arrays.
=> Ideal for dataframes, images, and large datasets.

3. Advanced Mathematical Operations:-
=> Supports statistical, algebraic, and matrix operations.
=> Includes mean, median, standard deviation, and linear algebra functions.

4. Efficient Data Storage & Memory Management:-
=> NumPy uses less memory than Python lists because it stores data in contiguous blocks.
=> Supports data types like int8, int16, float32, float64, allowing better memory usage.

5. Data Cleaning & Handling Missing Values:-
=> Replace missing values (NaN) easily using np.nan_to_num().
=> Perform data filtering & transformation with ease.

6. Integration with Pandas, Matplotlib & Machine Learning:-
=> Works seamlessly with Pandas (for DataFrames), Matplotlib (for visualization), and Scikit-learn (for ML).

Summary: Why Data Analysts Love NumPy?
=> Blazing Fast: NumPy is 50x faster than Python lists.
=> Handles Large Data: Supports multi-dimensional arrays for big datasets.
=> Advanced Analytics: Includes statistics, algebra, and matrix operations.
=> Memory Efficient: Uses less memory than traditional Python lists.
=> Seamless Integration: Works with Pandas, Matplotlib, and Scikit-Learn.

NumPy is an essential tool for Data Analysts, Data Scientists, and Machine Learning Engineers!
'''

# What is array?
'''
An array is a data structure used to store multiple values of the same data type in a single variable. Arrays allow efficient storage, access, and manipulation of data, making them essential for data analysis, machine learning, and scientific computing.
In Python, we typically use NumPy arrays instead of Python lists because NumPy arrays are faster, more memory-efficient, and support mathematical operations.
'''

# Why Use Arrays Instead of Lists?
'''
| ~Feature~	       |   ~Python_List~	        |   ~NumPy_Array~                       |
| Speed	           |   Slow (Loops required)	|   Fast (Vectorized operations)        |
| Memory	       |   Takes more space	        |   Efficient memory usage              |
| Math Operations  |   Requires loops	        |   Direct mathematical operations      |
| Data Type	       |   Can store mixed types	|   Stores same type (int, float, etc.) |
'''


'''Types of Arrays?'''

# # => 1D Array (Vector) :- A 1D array stores elements in a single row.
# import numpy as np
# arr1d = np.array([1, 2, 3, 4, 5])
# print("1D Array\n",arr1d)

# # => 2D Array (Matrix) :- A 2D array is a table with rows and columns.
# import numpy as np
# arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("\n2D Array\n",arr2d)

# # => 3D Array (Multi-Dimensional) :- A 3D array is used for storing multiple 2D arrays (e.g., images, scientific data).
# import numpy as np
# arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("\n3D Array\n",arr3d)


'''Array Properties:- '''

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print("Shape of Array ",arr.shape)   # Shape (size of dimensions)
# print("Dimesnion of Array",arr.ndim)    # Number of dimensions (1D, 2D, 3D)
# print("Number of elements of Array",arr.size)    # Total number of elements
# print("Data type of Array",arr.dtype)   # Data type (int, float, etc.)


'''Array Operations'''
# # NumPy allows fast mathematical operations without loops!
# import numpy as np
# arr = np.array([10, 20, 30])
# print(arr + 5)  # Add 5 to each element -> [15 25 35]
# print(arr * 2)  # Multiply each element by 2 -> [20 40 60]
# print(arr ** 2) # Square each element -> [100 400 900]

'''Summary of Array'''
# => An array is a collection of elements stored in a single variable.
# => NumPy arrays are faster and more memory-efficient than Python lists.
# => Supports 1D, 2D, and 3D arrays for data analysis and machine learning.
# => Enables fast mathematical operations without loops.