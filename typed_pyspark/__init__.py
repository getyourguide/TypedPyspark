from __future__ import annotations

import typing
from typing import Any, Generic, List, NewType, TypeVar, get_type_hints

from pyspark.sql import DataFrame as DataFrameOrig


class DataFrame:
    """
    TypedDataFrame abstraction
    """

    def __class_getitem__(cls, *args, **kwargs):
        df_class = type("DataFrame", (DataFrame,), {})

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


def validate(func):
    """ validate dataframe objects """

    def wrap(*args, **kwargs):
        breakpoint()
        result = func(*args, **kwargs)
        return result

    return wrap
