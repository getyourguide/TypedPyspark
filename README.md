# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:

- Define dataframe schemas and use them as annotations in variables, functions, classes
- Validate them in realtime with the @validate_dataframes functionality
- Type check them statically (mypy support)

#  Rationale

Projects using spark that follow software engineering best practices is common to see
functions defined with type annotations like this:

```py
from pyspark.sql import DataFrame

def get_name_from_id(dt: DataFrame) -> DataFrame:
    ...
```

But this type annotation only guarantees that a DataFrame instance is called.
It says nothing about important information about the dataframe.

1. If the columns needed are there
2. If they have the correct types
3. If there are much more data than needed

This library tries to address exactly these problems.
With it you can do something like the following:

# Usage

```py
from typed_pyspark import DataFrame, validate_dataframes

@validate_dataframes
def get_name_from_id(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
    ...
```

By running it you get type errors when the annotations dont match reality.
You also get self-documenting code in form of expressive annotations.

# Install

```sh
pip install typed-pyspark
```


## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
