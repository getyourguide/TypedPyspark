# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:


- Define dataframe type annotation for functions and return types
- Type check them


# Install

pip install typed_pyspark


#  Usage

The library allows you to write code like this:

```py
@validate_dataframes
def get_name_right(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
    return dt.withColumn("name", F.lit("abc"))
```

And get type errors when the annotations dont match reality.


## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
