from __future__ import annotations

import datetime
from typing import List, Optional, TypeVar

from pyspark.sql import DataFrame as DataFrameOrig
from pyspark.sql import SparkSession


def create_datetime(x, format="%Y-%m-%dT%H:%M:%SZ"):
    return datetime.datetime.strptime(x, format)


def assert_expected_like_result(expected_df, result_df):
    assert_dfs_are_equal(expected_df, result_df.select(expected_df.columns))


def assert_identical_content(df1, df2):
    if df1.collect() != df2.collect():
        df1.show()
        df2.show()
        raise Exception("Dataframes differ in the content")
    return True


def assert_dfs_are_equal(df1, df2) -> bool:
    if df1.schema != df2.schema:
        df1.printSchema()
        df2.printSchema()
        raise Exception("Dataframes differ in the schema")

    assert_identical_content(df1, df2)

    return True


class Dataframe:
    default_values: dict = {}
    schema: dict = {}

    def create_df(
        self, data: List[dict], schema=None, default_values: Optional[dict] = None
    ):

        entries = []
        default_values = (
            {**default_values, **self.default_values}
            if default_values
            else self.default_values
        )

        # merge rows with default values
        for row in data:
            row = {**default_values, **row}
            entries.append(row)

        schema = schema if schema else self.schema

        spark = SparkSession.builder.getOrCreate()
        df = spark.createDataFrame(entries, schema=self.schema_to_str(schema))
        return df

    def __init__(self, schema, default_values=default_values):
        self.schema = schema
        self.default_values = default_values

    @property
    def columns(self) -> List[str]:
        """
        IDE Auto-complete suggests that we can call this method, but it needs to be implemented here.
        Returns a list of all column names.
        """
        return list(self.schema.keys())

    @staticmethod
    def schema_to_str(a_dict):
        result = "".join(key + " " + value + "," for key, value in a_dict.items())
        result = result[:-1]
        return result

    @classmethod
    def type_annotation(cls):
        return TypeVar("DataFrame", cls, DataFrameOrig)
