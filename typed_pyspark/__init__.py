from __future__ import annotations

import typing
from typing import Any, Generic, List, NewType, TypeVar, get_type_hints

from pyspark.sql import DataFrame as DataFrameOrig


class DataFrame:
    def __class_getitem__(cls, *args, **kwargs):
        return DataFrame

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
    print(func.__annotations__)

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrap
