from __future__ import annotations

from typing import Any


def validate(func):
    print(func.__annotations__)

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrap


class DataFrame:
    def __class_getitem__(cls, *args, **kwargs):
        df = DataFrame
        df.schema = {}
        df.schema["args"] = args
        df.schema["kwargs"] = kwargs

        return df


phone = str
url = str


def test_first():
    df_names = DataFrame["phone", "url", ...]

    @validate
    def test(df: df_names) -> DataFrame["phone", "url"]:
        return DataFrame()

    test(DataFrame())
