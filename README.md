# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:

- Define dataframe schemas and use them as annotations in variables, functions, classes
- Validate them in realtime with the @validate_dataframes functionality
- Type check them statically (mypy support)

#  Rationale

Projects using spark that follow software engineering best practices is common to see
functions defined with type annotations this:

```py
from pyspark.sql import DataFrame

def get_name_right(dt: DataFrame) -> DataFrame:
    return dt.withColumn("name", F.lit("abc"))
```

But this type annotation only guarantees that a DataFrame instance is called, it says nothing about the content of the dataframe.
If the columns needed in the function are actually there we can only know by running the function and see if it breaks.
If there are much more columns than expected nobody will know. We cannot also say anything about the types of the columns.

This library tries to address exactly these problems, with it you can do something like the following:

# Usage

```py
from typed_pyspark import DataFrame, validate_dataframes

@validate_dataframes
def get_name_right(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
    return dt.withColumn("name", F.lit("abc"))
```

And get type errors when the annotations dont match reality.

# Install

```sh
pip install typed_pyspark
```


## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
