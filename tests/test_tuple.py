from typing import NamedTuple, NewType, Tuple

DataFrame = Tuple


class DataFrameType(Tuple):
    def __new__(self, x):
        self.x = x


def test_types():
    a_df = DataFrame[int, str]

    def a_test(x: a_df) -> DataFrame[int]:
        return DataFrameType(1)

    result: DataFrame[int] = a_test()


def test_columns():
    a_df = DataFrame["name"]
    b_df = DataFrame["name", "age"]

    def new_test(x: a_df) -> b_df:
        return DataFrameType("123")

    new_test()
