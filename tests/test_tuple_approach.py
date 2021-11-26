"""

Pros-cons approach

Pros:

- mypy works like a charm


Cons:
- could not find a way to have a specific type in the __annotations__ now is looking like tuple

"""
from typing import Any, NamedTuple, NewType, Tuple

DataFrame = Tuple


def validate(func):
    print(func.__annotations__)

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrap


class DataFrameType(Tuple):
    def __new__(self, *args, **kwargs):
        pass


def test_validate():
    a_df = DataFrame[int, str]
    b_df = DataFrame["name", "age", Any]

    @validate
    def with_validation(x: a_df) -> b_df:
        return DataFrameType()

    with_validation(DataFrameType())


def test_types():
    a_df = DataFrame[int, str]

    def a_test(x: a_df) -> DataFrame[int]:
        return DataFrameType(1)

    result: DataFrame[int] = a_test(DataFrameType())


def test_columns():
    a_df = DataFrame["name"]
    b_df = DataFrame["name", "age"]

    def new_test(x: a_df) -> b_df:
        return DataFrameType("123")

    new_test(DataFrameType())
