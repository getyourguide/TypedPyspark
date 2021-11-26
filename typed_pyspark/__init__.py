from __future__ import annotations

import typing
from typing import Any, Generic, List, NewType, TypeVar, get_type_hints

from pyspark.sql import DataFrame as DataFrameOrig


class DataFrame:
    """
    TypedDataFrame abstraction
    """

    def __class_getitem__(cls, *args, **kwargs):
        # 'inherits a new type from dataframe base type'
        df_class = type("TypedDataFrame", (DataFrame,), {})

        df_class.schema = {}
        df_class.schema["args"] = args
        df_class.schema["kwargs"] = kwargs

        return df_class

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def from_data(cls, data: List[dict]) -> List["DataFrame"]:
        result = []
        for row in data:
            rowobj = cls(**row)
            result.append(rowobj)

        return result


class InvalidSchemaException(Exception):
    pass


def validate_dataframes(func):
    """ validate all dataframes available in a function"""

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)

        if (
            "return" in func.__annotations__
            and DataFrame in func.__annotations__["return"].__bases__
        ):
            columns_expected = set(func.__annotations__["return"].schema["args"][0])
            columns_got = set(result.columns)

            if columns_expected != columns_got:
                raise InvalidSchemaException(
                    f"Return Schema different, got: {columns_got}, expected: {columns_expected}"
                )

        return result

    return wrap
