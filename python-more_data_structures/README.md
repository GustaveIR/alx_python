# Matrix Squaring Function

## Description

This Python program defines a function that computes the square value of all integers in a matrix. It provides a way to create a new matrix where each element is the square of the corresponding element in the input matrix.

## Function

### `square_matrix_simple(matrix)`

Computes the square value of all integers in the input matrix and returns a new matrix with squared values. The input matrix remains unchanged.

#### Arguments

- `matrix` (list of lists): The input 2-dimensional array (matrix) containing integers.

#### Returns

- `new_matrix` (list of lists): A new matrix with squared values. Each value in the new matrix is the square of the corresponding value in the input matrix.

## Usage

To use the `square_matrix_simple` function, import it and provide the input matrix as an argument. The function will return a new matrix with squared values.

Example:

```python
from square_matrix_simple import square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
