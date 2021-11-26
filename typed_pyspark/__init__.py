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
        Validator.validate_args(func, args, kwargs)
        result = func(*args, **kwargs)
        Validator.validate_result(func, result)
        return result


    return wrap


class Validator:
    @staticmethod
    def validate_args(func, args, kwargs):

        expected_dataframe_arguments = [x for x in func.__annotations__ if x != 'return' and DataFrame  in
                                        func.__annotations__[x].__bases__]

        if not len(expected_dataframe_arguments):
            return

        args_to_be_validated = [arg for arg in args if isinstance(arg, DataFrameOrig)]

        if len(expected_dataframe_arguments) != len(args_to_be_validated):
            raise InvalidSchemaException(f"Expected : {len(expected_dataframe_arguments)} dataframes got only {len(args_to_be_validated)}")


        for i in range(0, len(args_to_be_validated)):
            columns_got = set(args_to_be_validated[i].columns)
            columns_expected = set(func.__annotations__[expected_dataframe_arguments[i]].schema["args"])

            if columns_expected != columns_got:
                raise InvalidSchemaException(
                    f"Return Schema different, got: {columns_got}, expected: {columns_expected}"
                )



    @staticmethod
    def validate_result(func, result):
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
