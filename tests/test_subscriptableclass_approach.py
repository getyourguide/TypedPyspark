from __future__ import annotations

from typing import Any

from pyspark.sql import SparkSession


def validate(func):
    print(func.__annotations__)

    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrap


class DataFrame:
    def __class_getitem__(cls, *args, **kwargs):
        return DataFrame


phone = str
url = str


def test_with_spark():
    df_names = DataFrame["phone", "url", ...]
    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"phone": "1233125"}])

    df.show()

    @validate
    def test(df: df_names) -> DataFrame["phone", "url"]:
        return df

    test(df)


def test_first():
    df_names = DataFrame["phone", "url", ...]

    @validate
    def test(df: df_names) -> DataFrame["phone", "url"]:
        return DataFrame()

    test(DataFrame())
