# Weight Converter
[![codecov](https://codecov.io/gh/adamriaz/weight-converter/branch/main/graph/badge.svg?token=hcHbzXWhUJ)](https://codecov.io/gh/adamriaz/weight-converter)
[![Documentation Status](https://readthedocs.org/projects/weight-converter/badge/?version=latest)](https://weight-converter.readthedocs.io/en/latest/?badge=latest)

A python module for converting weight units.

## Install
To install Weight Converter, run the following command:
```bash
pip install weight-converter
```

## Usage
Import the module and unit class
```python
from weight_converter.convert import Kilograms

kilograms = Kilograms(value=1)
lbs = kilograms.to_pounds()
```


