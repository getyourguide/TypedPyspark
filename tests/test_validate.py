from typing import Any, TypeVar

import pyspark.sql.functions as F
import pytest
from pyspark.sql import DataFrame as DataFrameOrig
from pyspark.sql import SparkSession

from typed_pyspark import (DataFrame, InvalidSchemaException,
                           validate_dataframes, wrap_with_generic)


def test_wrong_argument_type():
    id = Any
    name = Any

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"wrong_col": "123"}])

    @validate_dataframes
    def wrong_col(dt1: DataFrame["id"]):
        return dt1

    with pytest.raises(InvalidSchemaException):
        wrong_col(df)


def test_arguments_number():
    id = Any

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"id": "123"}])

    @validate_dataframes
    def wrong_num_of_params(dt1: DataFrame["id"], dt2: DataFrame["id"]):
        return dt1

    with pytest.raises(InvalidSchemaException):
        # pass a dataframe and a non-dataframe where 2 dataframes are expected
        wrong_num_of_params(df)


def test_return():
    id = Any
    name = Any

    spark = SparkSession.builder.getOrCreate()
    df = spark.createDataFrame([{"id": "123"}])

    ReturnType = wrap_with_generic(DataFrame["id", "name"])

    @validate_dataframes
    def get_name_wrong(dt: DataFrame["id"]) -> DataFrame["id", "name"]:
        return dt

    with pytest.raises(InvalidSchemaException):
        get_name_wrong(df)

    @validate_dataframes
    def get_name_right(dt: DataFrame["id"]) -> ReturnType:
        return dt.withColumn("name", F.lit("abc"))

    get_name_right(df)
