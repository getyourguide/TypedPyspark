# TypedPyspark

Contains a set of abstractions to type dataframes in pyspark.

Allows one to:


- Define dataframe type annotation for functions and return types
- Type check them



# Usage

```

# create type annotaitons on the fly and apply it to functions

DataFrame["phone", "url"]
```


## Acknowledgements

Inspired by [dataenforce](https://github.com/CedricFR/dataenforce) which provides similar functionality for pandas.
