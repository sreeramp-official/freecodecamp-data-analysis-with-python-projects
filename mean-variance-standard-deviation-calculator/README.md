# Mean-Variance-Standard Deviation Calculator

This project is part of the **Data Analysis with Python** course by FreeCodeCamp. It involves building a Python function to calculate statistical metrics for a 3x3 matrix.

## Features

The `calculate()` function computes the following statistics for a 3x3 matrix derived from a 9-element list:
- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

Each metric is calculated for:
1. Rows (axis 1)
2. Columns (axis 0)
3. Flattened matrix

## Usage

### Input
A list of exactly 9 numbers (e.g., `[0, 1, 2, 3, 4, 5, 6, 7, 8]`).

### Output
A dictionary with the following structure:
```python
{
  'mean': [axis0, axis1, flattened],
  'variance': [axis0, axis1, flattened],
  'standard deviation': [axis0, axis1, flattened],
  'max': [axis0, axis1, flattened],
  'min': [axis0, axis1, flattened],
  'sum': [axis0, axis1, flattened]
}
```

### Example
```python
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

## Setup

1. Install Python and NumPy if not already installed:
   ```bash
   pip install numpy
   ```

2. Run the `main.py`.

## Error Handling
If the input list contains fewer or more than 9 elements, the function raises a `ValueError` with the message:
```
List must contain nine numbers.
