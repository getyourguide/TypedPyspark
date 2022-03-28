# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:

- Define dataframe schemas and use them as annotations in variables, functions, classes
- Create mock data for tests easily based on these schemas

#  Rationale

In Projects using spark that follow software engineering best practices is common to see
functions defined with type annotations like this:

```py
from pyspark.sql import DataFrame

def get_name_from_id(dt: DataFrame) -> DataFrame:
    ...
```

But this type annotation only guarantees that a DataFrame instance is called.
It says nothing about how the dataframe looks like.

1. If the columns needed are there
2. If they have the correct types
3. If there are much more data than needed

This library tries to address exactly these problems.
By running it you get type errors when the annotations dont match reality.
You also get self-documenting code in form of expressive annotations.

# Install

```sh
pip install 'typed-pyspark~=0.0.4'
```

## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
