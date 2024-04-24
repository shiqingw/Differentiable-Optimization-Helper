# Differentiable-Optimization-Helper

This is a helper library for differentiable optimization problems. It only supports the ellipsoid-ellipsoid (or ellipse-ellipse) to the second order.

## Installation
1. Clone the repository
```bash
git clone https://github.com/shiqingw/Differentiable-Optimization-Helper.git
```

2. Install the dependencies
```bash
conda activate <your_env>
pip install numpy
pip install pybind11
conda install -c conda-forge xtensor
conda install -c conda-forge xtensor-blas
conda install -c conda-forge xtensor-python
```

3. Build and install DiffOptHelper
```bash
cd Differentiable-Optimization-Helper
pip install .
```

## Test
Test the installation in a python script
```python
import diffOptHelper as doh
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(doh.getDualVariable(a, b))
```
